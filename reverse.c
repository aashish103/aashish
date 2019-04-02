#include<stdio.h>

int main()
{
  
int n;
  
printf("Enter n:");
  
scanf("%d",&n);
  
int r,s=0;
  

  
while(n>0)
 
{
    
r=n%10;
   
s=s*10+r;
    
n=n/10;
  
}
   


 printf("Reverse Number:"s);
 return 0;
 }
 
 
