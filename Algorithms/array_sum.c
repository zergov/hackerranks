#include <stdio.h>
#include <stdlib.h>

int simpleArraySum(int n, int ar_size, int* ar) {
    int result = 0;
    while(n-- > 0) {
        result += *ar++;
    }

    return result;
}

int main() {
    int n;
    scanf("%i", &n);

    int *ar = malloc(sizeof(int) * n);
    for(int ar_i = 0; ar_i < n; ar_i++){
       scanf("%i",&ar[ar_i]);
    }

    printf("%d\n", simpleArraySum(n, n, ar));
    return 0;
}
