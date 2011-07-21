#include <stdio.h>

int main(int argc, char *argv[]) {

	if (argc != 2) {
		printf("Not enough arguments...\n");
		return 1;
	}

	int total;
	int p100, p50, p20, p10, p5, p2;
	int tp100, tp50, tp20, tp10, tp5, tp2;
	int combo = 1; // for the single 200 pence combination
	

	total = atoi(argv[1]);
	
	for (p100 = 0; p100 <= total/100; p100++) {
		tp100 = total - p100*100;
		for(p50 = 0; p50 <= tp100/50; p50++) {
			tp50 = tp100 - p50*50;
			for (p20 = 0; p20 <= tp50/20; p20++) {
				tp20 = tp50 - p20*20;
				for (p10 = 0; p10 <= tp20/10; p10++) {
					tp10 = tp20 - p10*10;
					for (p5 = 0; p5 <= tp10/5; p5++) {
						tp5 = tp10 - p5*5;
						for (p2 = 0; p2 <= tp5/2; p2++) {
							tp2 = tp5 - p2*2;
							combo++;
						}
					}
				}
			}
		}
	}
	printf("%d\n", combo);

	return 0;
}
