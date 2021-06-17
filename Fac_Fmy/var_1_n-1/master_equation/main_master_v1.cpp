#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<string>
#include<fstream>

#define N_s 100
#define t_max 10000
#define l_0 1.4e-6
#define Kb 1.38e-23
#define T 309.5
#define Fmy_0 0.01e-9
#define k_my 20.4
#define x_0 0.001e-6
#define A_ac 1.0e-4

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

double Force_actin(double length2){
  return A_ac*(length2 - l_0);
}

int main(void){

	srand((unsigned)time(NULL));

	double sarcomere[t_max][N_s];
  double x[N_s];
	double F_my[N_s];
  double F_ac[N_s];
	double F_all[N_s];
  double PP;
  double var[t_max];
  double sum;
  double ave;
  double result;
  double num_sum[N_s];
  double num_result[N_s];
  double num_ave[N_s];
  double num_var[N_s];
  double F_sum[t_max];
  double F_ave[t_max];

	FILE* fp0;
	fp0 = fopen("s_N100_Ae4_x0001e6_tmax10000.dat","w");
	if(fp0==NULL){
		printf("File open faild.");
	}

	FILE* fp1;
	fp1 = fopen("s_var_N100_Ae4_x0001e6_tmax10000.dat","w");
	if(fp1==NULL){
		printf("File open faild.");
	}

  FILE* fp2;
  fp2 = fopen("t_F_N100_Ae4_x0001e6_tmax10000.dat","w");
  if(fp2==NULL){
    printf("File open faild");
  }

  for(int ini=0; ini<N_s; ini++){
	  x[ini] = ini*l_0;

    if(ini != 0 and ini != N_s -1){
      x[ini] += randGauss(Uniform(), Uniform(), x_0);
    }
  }

/*
  for(int ini=0; ini<N_s - 1; ini++){

    sarcomere[0][ini] = x[ini + 1] - x[ini];
    F_my[ini] = Force_myosin(sarcomere[0][ini]);
    printf("%15e\n",sarcomere[0][ini]);
  } 
*/
  for(int num_i=0; num_i<N_s; num_i++){
    num_sum[num_i] = 0.0;
  }

  for(int t_run=0; t_run<t_max; t_run++){
    F_sum[t_run] = 0.0;
  }

  double t=0.0;
	for(int iter=0; iter<t_max; iter++){
    printf("t=%d\n",t);

    for(int num=0; num<N_s-1; num++){
      sarcomere[t][num] = x[num + 1] - x[num];
      //printf("sarcomere=%15e\n",sarcomere[t][num]);
      //printf("%15e\n",sarcomere[num]);
      F_my[num] = Force_myosin(sarcomere[t][num]);
      F_ac[num] = Force_actin(sarcomere[t][num]);
    }
  

    sum = 0.0;
    for(int i=1; i<N_s - 2; i++){
      sum += sarcomere[t][i];
    }
    
    //printf("sum=%15e\n",sum);
    ave = sum/((double)N_s - 3.0);
    //printf("ave=%15e\n",ave);

    result = 0.0;
    for(int i=1; i<N_s - 2; i++){
      result += (sarcomere[t][i] - ave)*(sarcomere[t][i] - ave);
    }
    
    var[t] = sqrt(result);

    fprintf(fp0, "%d\t%15e\t%15e\t%15e\n" ,t,sarcomere[t][3],sarcomere[t][N_s/2],var[t]);
    //printf("t=%d\tl_edge=%15e\tl_center=%15e\tver=%15e\n",t,sarcomere[t][3],sarcomere[t][N_s/2],var[t]);


    for(int num_i=0; num_i<N_s - 1; num_i++){
      num_sum[num_i] += sarcomere[t][num_i];
    }

    for(int num=0; num<N_s - 1; num++){

      F_all[num] = F_my[num];
      F_sum[t] += F_all[num]; 
      
      double value = Uniform();
      PP = Fluctuation_theorem(F_all[num]);

      if(value < 1 / (1 + PP)){
        if(num != 0){
          x[num] += 0.5*x_0;
          x[num + 1] -= 0.5*x_0;
        }
      }
      else{
        if(num != 0){
          x[num] -= 0.5*x_0;
          x[num + 1] +=0.5*x_0;
        }
      }

    }

    F_ave[t] = F_sum[t]/(N_s - 1);
    fprintf(fp2, "%d\t%15e\t%15e\t%15e\n",t,F_all[4],F_all[N_s/2],F_ave[t]);

  }	

  for(int num=0; num<N_s - 1; num++){
    num_result[num] = 0.0;
  }

  for(int num=1; num<N_s - 2; num++){
    num_ave[num] = num_sum[num]/((double)N_s - 3.0);

    for(int t_num=0; t_num<t_max; t_num++){
     num_result[num] += (sarcomere[t_num][num] - num_ave[num])*(sarcomere[t_num][num] - num_ave[num]);
    }
  num_var[num] = sqrt(num_result[num]);
  fprintf(fp1, "%d\t%15e\n",num,num_var[num]);
  //printf("n=%d\tnum_var=%15e\n",num,num_var[num]);
  }

 
  

	fclose(fp0);
  fclose(fp1);
  fclose(fp2);
	return 0;
}
