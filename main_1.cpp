#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
#include<string>
#include<fstream>

#define N_s 200
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


int main(void){

	srand((unsigned)time(NULL));

	double sarcomere[t_max][N_s];
  double x[N_s];
	double F_my[N_s];
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

	FILE* fp0;
	fp0 = fopen("N200_x001e6_tmax100.dat","w");
	if(fp0==NULL){
		printf("File open faild.");
	}

	FILE* fp1;
	fp1 = fopen("ver_N200_x001e6_tmax100.dat","w");
	if(fp1==NULL){
		printf("File open faild.");
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

	for(int t=0; t<t_max; t++){
    printf("t=%d\n",t);

    for(int num=0; num<N_s-1; num++){
      sarcomere[t][num] = x[num + 1] - x[num];
      //printf("sarcomere=%15e\n",sarcomere[t][num]);
      //printf("%15e\n",sarcomere[num]);
      F_my[num] = Force_myosin(sarcomere[t][num]);
    }
  

    sum = 0.0;
    for(int i=0; i<N_s - 1; i++){
      sum += sarcomere[t][i];
    }
    
    //printf("sum=%15e\n",sum);
    ave = sum/((double)N_s - 1.0);
    //printf("ave=%15e\n",ave);

    result = 0.0;
    for(int i=0; i<N_s - 1; i++){
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

  }	

  for(int num=0; num<N_s - 1; num++){
    num_result[num] = 0.0;
  }
  for(int num=0; num<N_s - 1; num++){
    num_ave[num] = num_sum[num]/((double)N_s - 1.0);

    for(int t_num=0; t_num<t_max; t_num++){
     num_result[num] += (sarcomere[t_num][num] - num_ave[num])*(sarcomere[t_num][num] - num_ave[num]);
    }
  num_var[num] = sqrt(num_result[num]);
  fprintf(fp1, "%d\t%15e\n",num,num_var[num]);
  //printf("n=%d\tnum_var=%15e\n",num,num_var[num]);
  }

 
  

	fclose(fp0);
  fclose(fp1);
	return 0;
}
