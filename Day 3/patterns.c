// floydtriangle is done with fibonaci series...
#include <stdio.h>

int main()
{
    int rows, i, j, number = 1;

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    for (i = 1; i <= rows; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%d ", number);
            // Incrementing the number for each iteration of the inner loop
            number++;
        }
        printf("\n");
    }

    return 0;
}
