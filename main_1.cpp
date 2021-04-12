#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<string>
#include<fstream>

#define N_s 10
#define t_max 100
#define l_0 1.4e-6
#define Kb 1.38e-23
#define T 309.5
#define Fmy_0 0.01e-9
#define k_my 10.2
#define x_0 0.01e-6

double Uniform(){
	return ((double)rand()+1.0)/((double)RAND_MAX+2.0);
}

double randGauss(double value1, double value2, double sigma){
	return sigma*sqrt(-2.0*log(value1))*sin(2.0*M_PI*value2);
}

int main(void){

	srand((unsigned)time(NULL));

	double sarcomere[N_s];
	double F_my[N_s];
	double F_all[N_s];

	FILE* fp0;
	fp0 = fopen("tmax100.dat","w");
	if(fp0==NULL){
		printf("File open faild.");
	}

	sarcomere[0] = 0;
	for(int i=0; i<t_max; i++){
		for(int ini=0; ini<N_s; ini++){
			sarcomere[ini] += l_0 + randGauss(Uniform(), Uniform(), x_0);
		}

		

		
	
	return 0;
}
