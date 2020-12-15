/****************************************************************************
 * RF-Score_desc.c (all rights reserved): This program reads a list of      *
 *                 PDBbind protein-ligand complexes and calculate their     *
 *                 RF-Score descriptors                                     *
 *                                                                          *
 * Author:        Dr Pedro J. Ballester                                     *
 *                                                                          *
 * Purpose:       Preprocessing PBDbind protein-ligand complexes            *
 *                                                                          *
 * Usage:         Read Appendix_A1.doc                                      * 
 *                                                                          *
 ****************************************************************************/

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NATOMAX  3500   /*  maximum number of heavy atoms in the bindsite */
#define NLIGATMAX 250   /*  maximum number of heavy atoms in the ligand */
#define NELEMTS    54   /*  maximum number of chemical elements considered */
#define DCUTOFF    12   /*  distance cutoff for protein atoms near ligand */

#define NLINES    200   /*  number of characters read per line in pdb file (ok?) */
#define NCNAME     60   /*  number of characters for file name (ok?) */
#define VERBOSE     0   /*  Show information about run? */

struct pdb_line         /*  template to store a PDB line */
{
    char  lineid[6];       
    int   atomid;           
    char  atomtype[5];             
    char  resname[4];
    char  chainid[2];              
    int   resid;
    float r[3];          
    float prob;         
    float dum;
    char  atomname[4];
    int   natoms; 
    int   atomnumber;
} pdbline;

struct ligand          /* template to store a ligand (also, used for binding site */
{
    int   natoms;
    int   atomid[NATOMAX];       
    char  atomtype[NATOMAX][5];             
    char  resname[4];
    char  chainid[2];              
    int   resid;
    float r[NATOMAX][3];          
    char  atomname[NATOMAX][4];
    int   atomnumber[NATOMAX];
    float bindaff;                
} ligand, bindsite;

typedef struct pdb_line PDB_LINE;
typedef struct ligand   LIGAND;

#include "RF-Score_desc.h"

int main(void)
{
    int icount = 0, iatom = 0;
    int i = 0, j = 0, k = 0, l = 0, m = 0, mmax = 0, ipdb = 0;
    int ind[NELEMTS][NELEMTS]={0}; /* 30 possible atomic numbers; correct this and next */
    float ddum, bindaff;
    char line[NLINES];    /* Line of data from the input file */
    char pdb_fname[4], dir[] = "v2007";
    char protfile[NCNAME], ligfile[NCNAME], pdbbind[NCNAME]; 
    FILE *finput, *fsettings, *fdescript, *fligand;
 
    /*
       Reading list of complexes (without extension .pdb)
     */
    fsettings = fopen("PDBbind_core07.txt", "r");
    if(fsettings == NULL)
        fprintf(stderr, "\n CANNOT OPEN .txt input file");  
        
    fdescript = fopen("PDBbind_core07.csv", "w");
    if(fdescript == NULL)
        fprintf(stderr, "\n CANNOT OPEN the .csv output file");
    
    /* Write header in file naming descriptors */
    fprintf(fdescript, "pbindaff");
    for(k = 0; k < NELEMTS; k++)
      for(l = 0; l < NELEMTS; l++)
        if( ( (l>=6) && (l<=9) ) || ( (l>=15) && (l<=17) ) || (l==35) || (l==53))
          if( ( (k>=6) && (k<=9) ) || ( (k>=15) && (k<=17) ) || (k==35) || (k==53) )
            fprintf(fdescript, ",%d.%d", l, k);
    fprintf(fdescript, ",PDB");
    fprintf(fdescript, "\n");
        
    while(fgets(line, NCNAME, fsettings) != NULL)
    {
       sscanf(line, "%4s %f\n", &pdb_fname, &bindaff);
       if(VERBOSE) printf("%s %f\n", pdb_fname, bindaff);

       for(i = 0; i < 30; i++) protfile[i] = '\0';
       for(i = 0; i < 5; i++)   protfile[i] = dir[i];
       strcat(protfile, "\\");
       for(i = 6; i < 10; i++)  protfile[i] = pdb_fname[i-6];
       strcat(protfile, "\\");
       for(i = 11; i < 15; i++) protfile[i] = pdb_fname[i-11];
       finput = fopen(strcat(protfile,"_protein.pdb"), "r"); 
       if(finput == NULL)
         fprintf(stderr, "\n CANNOT OPEN %s", protfile);
    
       for(i = 0; i < 30; i++) ligfile[i] = '\0';
       for(i = 0; i < 5; i++)   ligfile[i] = dir[i];
       strcat(ligfile, "\\");
       for(i = 6; i < 10; i++)  ligfile[i] = pdb_fname[i-6];
       strcat(ligfile, "\\");
       for(i = 11; i < 15; i++) ligfile[i] = pdb_fname[i-11];
       fligand = fopen(strcat(ligfile,"_ligand.sdf"), "r");
       if(fligand == NULL)
         fprintf(stderr, "\n CANNOT OPEN %s", ligfile);
        
       printf("\nPDB:\t%d\n\n", ipdb+1);
       printf("INPUT  PDB PROTEIN:\t%s\n",       protfile);
       printf("INPUT  SDF LIGAND:\t%s\n",        ligfile);
       printf("\n");
        
       /*
         Read current ligand from SDF file
       */
       icount = 0; iatom = 0;
       while(fgets(line, NLINES, fligand) != NULL)
       {
         /*
             1st line in SDF file contains ligand id
          */
         if(icount == 0)
         {
            /* Read drug ids from SDF file */
            sscanf(line, "%4s\n", &ligand.resname);
            if(VERBOSE)
               printf("Ligand %4s_ligand.sdf\n", ligand.resname);
         }

         /*
            3rd line in each molecule contains #of atoms 
          */
         if(icount == 3)
         {
            sscanf(line, "%3d\n", &ligand.natoms);
            if(ligand.natoms > NLIGATMAX)  /* then correct reading error */
            {
                sscanf(line, "%2d\n", &ligand.natoms);
                if(VERBOSE) printf("Reading error corrected: Ligand has now %d atoms\n", ligand.natoms);
                if(VERBOSE) printf("%s\n", line);
            }
            if(VERBOSE)
                printf("--> It has %d atoms\n\n", ligand.natoms);
         }

         /*
            Reading atom's coordinates in current molecule 
          */
         if((icount > 3) && (icount < ligand.natoms + 4))
         {
            iatom = icount - 4;
            sscanf(line, "%f %f %f %s\n", 
               &ligand.r[iatom][0], &ligand.r[iatom][1], &ligand.r[iatom][2], &ligand.atomname[iatom]);
            ligand.atomnumber[iatom] = atomnumber(ligand.atomname[iatom]);
             
            if(VERBOSE)
                printf("atom=%d\t r[0]=%f\t r[1]=%f\t r[2]=%f\t %s  %d\n", 
                   iatom + 1, ligand.r[iatom][0], ligand.r[iatom][1], ligand.r[iatom][2], 
                   ligand.atomname[iatom], ligand.atomnumber[iatom]);
         }
         icount = icount + 1;
       }
       ligand.bindaff = bindaff;
       if(VERBOSE) printf("Binding affinity=%f\n", bindaff);
       fclose(fligand);
         
       /* Extract binding site for current ligand */
       iatom = 0;
       while(fgets(line, NLINES, finput) != NULL)
       {
          if(!strncmp(line,"ATOM",4))  
          { 
             sscanf(line, "%6s%d%5s%4s%1s%d %f %f %f %f %f %2s\n", 
                &pdbline.lineid, &pdbline.atomid, &pdbline.atomtype, &pdbline.resname, 
                &pdbline.chainid, &pdbline.resid, &pdbline.r[0], &pdbline.r[1], 
                &pdbline.r[2], &pdbline.prob, &pdbline.prob, &pdbline.dum);
             strncpy(pdbline.atomname, pdbline.atomtype, 4);
            
             k = 0;
             while(k != ligand.natoms) 
             {
                ddum = distance (ligand.r[k], pdbline.r);

                if(ddum < DCUTOFF)
                { 
                   if(VERBOSE) report_pdbline(pdbline);
                   bindsite.atomid[iatom]                        = pdbline.atomid;
                   bindsite.resid                                = pdbline.resid;
                   for(i = 0; i < 3; i++) bindsite.r[iatom][i]   = pdbline.r[i];
                   strncpy(bindsite.atomtype[iatom], pdbline.atomtype, 5);
                   strncpy(bindsite.resname, pdbline.resname, 4);
                   strncpy(bindsite.atomname[iatom], pdbline.atomname, 2);
                   bindsite.atomnumber[iatom] = atomnumber(pdbline.atomname);
                   
                   if(iatom > NATOMAX - 1) 
                      fprintf(stderr, "\nError: Binding site has %d atoms (predefined limit is %d)\n", iatom+1, NATOMAX);
                   iatom++;
                   bindsite.natoms = iatom;   
                   break;
                }
                k++;
             }   
          }  
       }
       if(VERBOSE) printf("bindsite.natoms=%d ligand.natoms=%d \n", bindsite.natoms, ligand.natoms);
       /* Initialise counters for following iteration */
       icount = 0; iatom = 0;
       i = 0; j = 0; k = 0; l = 0; m = 0; mmax = 0; ipdb++;
       
       /* Calculate distances between current ligand and its binding site */
       for(j = 0; j < NELEMTS; j++) for(i = 0; i < NELEMTS; i++) ind[i][j] = 0;
          
       for(k = 0; k < ligand.natoms; k++)
       {
          for(l = 0; l < bindsite.natoms; l++)
          {
             ddum = distance (ligand.r[k], bindsite.r[l]);
             
             if(ddum < DCUTOFF)
             { 
                    mmax = ind[bindsite.atomnumber[l]][ligand.atomnumber[k]];
                    mmax++;
                    ind[bindsite.atomnumber[l]][ligand.atomnumber[k]] = mmax;
             }
          }
       }
       
       if(VERBOSE) printf("\npK=%e\n", ligand.bindaff);
       if(VERBOSE) printf("\n-------------------\n");
       fprintf(fdescript,"%6.3f", ligand.bindaff); /* %6.3f pIC50  */
       for(k = 0; k < NELEMTS; k++)
       {
         for(l = 0; l < NELEMTS; l++)
         {
          if( ( (l>=6) && (l<=9) ) || ( (l>=15) && (l<=17) ) || (l==35) || (l==53))
          {
              if( ( (k>=6) && (k<=9) ) || ( (k>=15) && (k<=17) ) || (k==35) || (k==53) )
              {
                  if(VERBOSE) printf("%d\t%d\t%d\n", l, k, ind[l][k]);
                  fprintf(fdescript, ",%d", ind[l][k]);
              }
          }
         }
       } 
       fprintf(fdescript,",%s\n", ligand.resname);
       fclose(finput);
    }
    fclose(fdescript);
    fclose(fsettings);
    getchar();

    return 0;
}
