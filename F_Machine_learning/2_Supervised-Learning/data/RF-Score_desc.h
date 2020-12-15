/* This routine returns the atomic number of the introduced atom */
int atomnumber(char atomname[]);

int atomnumber(char atomname[])
{
 int atnum;

 if     (!strncmp(atomname, "C",4)) atnum = 6;
 else if(!strncmp(atomname, "CA",4)) atnum = 6;
 else if(!strncmp(atomname, "CB",4)) atnum = 6;
 else if(!strncmp(atomname, "CD",4)) atnum = 6;
 else if(!strncmp(atomname, "CD1",4)) atnum = 6;
 else if(!strncmp(atomname, "CD2",4)) atnum = 6;
 else if(!strncmp(atomname, "CE",4)) atnum = 6;
 else if(!strncmp(atomname, "CE1",4)) atnum = 6;
 else if(!strncmp(atomname, "CE2",4)) atnum = 6;
 else if(!strncmp(atomname, "CE3",4)) atnum = 6;
 else if(!strncmp(atomname, "CG",4)) atnum = 6;
 else if(!strncmp(atomname, "CG1",4)) atnum = 6;
 else if(!strncmp(atomname, "CG2",4)) atnum = 6;
 else if(!strncmp(atomname, "CH2",4)) atnum = 6;
 else if(!strncmp(atomname, "CZ",4)) atnum = 6;
 else if(!strncmp(atomname, "CZ2",4)) atnum = 6;
 else if(!strncmp(atomname, "CZ3",4)) atnum = 6;
 else if(!strncmp(atomname, "O",4)) atnum = 8;
 else if(!strncmp(atomname, "OD1",4)) atnum = 8;
 else if(!strncmp(atomname, "OD2",4)) atnum = 8;
 else if(!strncmp(atomname, "OE1",4)) atnum = 8;
 else if(!strncmp(atomname, "OE1A",4)) atnum = 8;
 else if(!strncmp(atomname, "OE1B",4)) atnum = 8;
 else if(!strncmp(atomname, "OE2",4)) atnum = 8;
 else if(!strncmp(atomname, "OG",4)) atnum = 8;
 else if(!strncmp(atomname, "OG1",4)) atnum = 8;
 else if(!strncmp(atomname, "OH",4)) atnum = 8;
 else if(!strncmp(atomname, "OXT",4)) atnum = 8;
 else if(!strncmp(atomname, "N",4)) atnum = 7;
 else if(!strncmp(atomname, "NE",4)) atnum = 7;
 else if(!strncmp(atomname, "NE1",4)) atnum = 7;
 else if(!strncmp(atomname, "NE2",4)) atnum = 7;
 else if(!strncmp(atomname, "NE2A",4)) atnum = 7;
 else if(!strncmp(atomname, "NE2B",4)) atnum = 7;
 else if(!strncmp(atomname, "ND1",4)) atnum = 7;
 else if(!strncmp(atomname, "ND2",4)) atnum = 7;
 else if(!strncmp(atomname, "NH1",4)) atnum = 7;
 else if(!strncmp(atomname, "NH2",4)) atnum = 7;
 else if(!strncmp(atomname, "NZ",4)) atnum = 7;
 else if(!strncmp(atomname, "P",4)) atnum = 15;
 else if(!strncmp(atomname, "S",4)) atnum = 16;
 else if(!strncmp(atomname, "SD",4)) atnum = 16;
 else if(!strncmp(atomname, "SG",4)) atnum = 16;
 else if(!strncmp(atomname,"Cl",4)) atnum = 17;
 else if(!strncmp(atomname, "H",4)) atnum = 1;
 else if(!strncmp(atomname, "HA",4)) atnum = 1;
 else if(!strncmp(atomname, "HA1",4)) atnum = 1;
 else if(!strncmp(atomname, "HA2",4)) atnum = 1;
 else if(!strncmp(atomname, "HB",4)) atnum = 1;
 else if(!strncmp(atomname, "HB1",4)) atnum = 1;
 else if(!strncmp(atomname, "HB2",4)) atnum = 1;
 else if(!strncmp(atomname, "HB3",4)) atnum = 1;
 else if(!strncmp(atomname, "HD1",4)) atnum = 1;
 else if(!strncmp(atomname, "HD2",4)) atnum = 1;
 else if(!strncmp(atomname, "HE",4)) atnum = 1;
 else if(!strncmp(atomname, "HE1",4)) atnum = 1;
 else if(!strncmp(atomname, "HE2",4)) atnum = 1;
 else if(!strncmp(atomname, "HE3",4)) atnum = 1;
 else if(!strncmp(atomname, "HG",4)) atnum = 1;
 else if(!strncmp(atomname, "HG1",4)) atnum = 1;
 else if(!strncmp(atomname, "HG2",4)) atnum = 1;
 else if(!strncmp(atomname, "HH2",4)) atnum = 1;
 else if(!strncmp(atomname, "HN1",4)) atnum = 1;
 else if(!strncmp(atomname, "HN2",4)) atnum = 1;
 else if(!strncmp(atomname, "HN3",4)) atnum = 1;
 else if(!strncmp(atomname, "HH",4)) atnum = 1;
 else if(!strncmp(atomname, "HZ",4)) atnum = 1;
 else if(!strncmp(atomname, "HZ1",4)) atnum = 1;
 else if(!strncmp(atomname, "HZ2",4)) atnum = 1;
 else if(!strncmp(atomname, "HZ3",4)) atnum = 1;
 else if(!strncmp(atomname, "1HD1",4)) atnum = 1;
 else if(!strncmp(atomname, "2HD1",4)) atnum = 1;
 else if(!strncmp(atomname, "3HD1",4)) atnum = 1;
 else if(!strncmp(atomname, "1HD2",4)) atnum = 1;
 else if(!strncmp(atomname, "2HD2",4)) atnum = 1;
 else if(!strncmp(atomname, "3HD2",4)) atnum = 1;
 else if(!strncmp(atomname, "1HE2",4)) atnum = 1;
 else if(!strncmp(atomname, "2HE2",4)) atnum = 1;
 else if(!strncmp(atomname, "1HG1",4)) atnum = 1;
 else if(!strncmp(atomname, "2HG1",4)) atnum = 1;
 else if(!strncmp(atomname, "3HG1",4)) atnum = 1;
 else if(!strncmp(atomname, "1HG2",4)) atnum = 1;
 else if(!strncmp(atomname, "2HG2",4)) atnum = 1;
 else if(!strncmp(atomname, "3HG2",4)) atnum = 1;
 else if(!strncmp(atomname, "1HH1",4)) atnum = 1;
 else if(!strncmp(atomname, "2HH1",4)) atnum = 1;
 else if(!strncmp(atomname, "1HH2",4)) atnum = 1;
 else if(!strncmp(atomname, "2HH2",4)) atnum = 1;
 else if(!strncmp(atomname, "F",4)) atnum = 9;
 else if(!strncmp(atomname, "B",4)) atnum = 5;
 else if(!strncmp(atomname,"Na",4)) atnum = 11;
 else if(!strncmp(atomname,"Mg",4)) atnum = 12;
 else if(!strncmp(atomname,"Al",4)) atnum = 13;
 else if(!strncmp(atomname, "K",4)) atnum = 19;
 else if(!strncmp(atomname,"Ca",4)) atnum = 20;
 else if(!strncmp(atomname, "V",4)) atnum = 23;
 else if(!strncmp(atomname,"M ",4)) atnum = 25;
 else if(!strncmp(atomname,"Fe",4)) atnum = 26;
 else if(!strncmp(atomname,"Co",4)) atnum = 27;
 else if(!strncmp(atomname,"Ni",4)) atnum = 28;
 else if(!strncmp(atomname,"Cu",4)) atnum = 29;
 else if(!strncmp(atomname,"Zn",4)) atnum = 30;
 else if(!strncmp(atomname,"As",4)) atnum = 33;
 else if(!strncmp(atomname,"Se",4)) atnum = 34;
 else if(!strncmp(atomname,"Br",4)) atnum = 35;
 else if(!strncmp(atomname,"Cd",4)) atnum = 48;
 else if(!strncmp(atomname, "I",4)) atnum = 53;
 else if(!strncmp(atomname,"Yb",4)) atnum = 70;
 else if(!strncmp(atomname,"Au",4)) atnum = 79;
 else if(!strncmp(atomname,"Hg",4)) atnum = 80;
 else if(!strncmp(atomname,"Pb",4)) atnum = 82;
 else if(!strncmp(atomname, "U",4)) atnum = 92;
 else
 { 
     printf("Error: Atomname %s not recognised\n", atomname); 
     getchar();
}
	
 return (atnum);
}						 		

/* Euclidean distance between two 3D vectors */
float distance(float*, float*);

float distance(float* vec1, float* vec2)
{
int i;
float dsum = 0.0, ddum = 0.0;

      for(i = 0; i < 3; i++)
      {
         ddum = vec1[i] - vec2[i];
         dsum += (ddum * ddum);
      }
      ddum = sqrt(dsum);
      
return (ddum);
}

/* Report a given line of the pdb file */
void report_pdbline(PDB_LINE struct1);

void report_pdbline(PDB_LINE struct1)
{

printf("%6s %d %5s %4s %1s %4d %f %f %f %3.2f %4.2f %2s\n", 
   struct1.lineid,  struct1.atomid, struct1.atomtype, struct1.resname, 
   struct1.chainid, struct1.resid,  struct1.r[0], struct1.r[1], struct1.r[2], 
   struct1.prob,    struct1.dum,    struct1.atomname );  

}

/* Write a given pdbline as ligand/binding site */
void write_molec(LIGAND *struct1, PDB_LINE struct2, int iatom);

void write_molec(LIGAND *struct1, PDB_LINE struct2, int iatom)
{
int i;

printf("sizeof(struct1)=%d\n", sizeof(struct1));
printf("sizeof(struct2)=%d\n", sizeof(struct2));

}
