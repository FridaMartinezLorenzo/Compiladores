#include <iostream>
  public class pruebaCompletaFinal{
public static void main(string args[]){
  int a,b;
   int vec[]=new int[10];
   int categ=2;
   float vecFloat[]={
2.3,5.0,3.1};
   float sueldo;
 cout<<"Teclea un numero:";
 cin>>a;
 b=a%2;
 if (b == 0 ){
cout<<a+" el numero es ";
 }
  float nsueldo=0;
 switch (categ){
case 1: nsueldo=sueldo*1.15;
 break;
 case 2: nsueldo=sueldo*1.10;
 break;
 }
  int n=0;
   int pot,suma=0;
 for (int i=0;
i <= n ;
i++){
pot=1;
 for (int j=0;
j < i ;
j++){
pot=pot*2;
 }
suma=suma+1/pot;
 }
  int i=0;
   float calif=0;
 while (i <= 4 ){
do {
cout<<"Teclea la calificacion %d:",i;
 cin>>calif;
 }
while (calif < 0 NoneNone calif > 10 );
 suma+=calif;
 i++;
 }
}
public static float suma(float a, float b){
return a+b;
 }
 