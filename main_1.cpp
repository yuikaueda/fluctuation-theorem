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
#define k_my 20.4
#define x_0 0.01e-6

double Uniform(){
	return ((double)rand()+1.0)/((double)RAND_MAX+2.0);
}

double randGauss(double value1, double value2, double sigma){
	return sigma*sqrt(-2.0*log(value1))*sin(2.0*M_PI*value2);
}

double Force_myosin(double length){
  return Fmy_0 - k_my*(length - l_0)*(length - l_0);
}

double Fluctuation_theorem(double force){
  return exp(force*x_0/(Kb*T));
}

double Variance(double s_length[N_s]){
  double sum = 0;
  for(int i=0; i<N_s; i++){
    sum += s_length[N_s];
  }

  double ave = sum/N_s;
  double result = 0;
  for(int i=0; i<N; i++){
    result += (s_length[i] - ave)*(s_length[i] - ave);
  }
  return result;
 
} 

int main(void){

	srand((unsigned)time(NULL));

	double sarcomere[N_s];
  double x[N_s];
	double F_my[N_s];
	double F_all[N_s];
  double PP;
  double var;

	FILE* fp0;
	fp0 = fopen("N10_tmax100.dat","w");
	if(fp0==NULL){
		printf("File open faild.");
	}

	x[0] = 0;
  for(int ini=1; ini<N_s - 1; ini++){
    x[ini] += l_0 + randGauss(Uniform(), Uniform(), x_0);
  }

  for(int ini=0; ini<N_s; ini++){
    sarcomere[ini] = x[ini + 1] - x[ini];
    F_my[ini] = Force_myosin(sarcomere[ini]);
  } 

	for(int t=0; t<t_max; t++){

    for(int num=0; num<N_s; num++){
      F_all[num] = F_my[num];
      
      double value = Uniform();
      PP = Fluctuation_theorem(F_all[num]);
      if(value < 1 / (1 + PP)){
        if(num != 0 and num != N_s - 1){
          x[num] += x_0/2;
          x[num + 1] -= x_0/2;
        }
      }
      else{
        if(num != 0 and num != N_s - 1){
          x[num] -= x_0/2;
          x[num + 1] += x_0/2;
        }
      }

      sarcomere[num] = x[num + 1] - x[num];
      F_my[num] = Force_myosin(sarcomere[num]);


    }
		

  }	
	
	return 0;
}
