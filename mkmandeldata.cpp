#include <iostream>
#include <string.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{

  int WIDTH=100;
  int HEIGHT=100;
  int MAXI=100;
  int JSON_LEN=WIDTH*HEIGHT*8+3;
  //double mb[WIDTH][HEIGHT];
  char json [JSON_LEN];
  strcat(json, "[");
  int i=0;
  while (i<WIDTH){
    strcat(json, "[");
    int j=0;
    while (j<HEIGHT){
      double c[]={(4.0/WIDTH)*i-2,(4.0/HEIGHT)*j-2};
      double z[]={0,0};
      double size=0;
      int inter=0;
      while ((size<4)&&(inter<MAXI)){
        double nz[2];
        nz[0]=z[0]*z[0]-z[1]*z[1]+c[0];
        nz[1]=2* z[0] * z[1] +c[1];
        z[0]=nz[0];
        z[1]=nz[1];
        size=z[0]*z[0]+z[1]*z[1];
        inter=inter+1;
      }
      if(size<4){
        //mb[i][j]=-1;
        strcat(json, "-1");
      }else{
        //mb[i][j]=inter;
        //ostringstream convert;   // stream used for the conversion
        //convert << inter;
        char Result[4];
        sprintf ( Result, "%d", inter );
        strcat(json, Result);
      }
      strcat(json, ",");
      j=j+1;
    }
    char Result2[4];
    sprintf ( Result2, "%d\n", i );
    std::cout << Result2;
    json[strlen(json) - 1] = '\0';
    strcat(json, "],");
    i=i+1;
  }
  json[strlen(json) - 1] = '\0';
  strcat(json, "]");
  //std::cout << json;

  ofstream file;
file.open ("mandeldata");
file << json;
file.close();
}
