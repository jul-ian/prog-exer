#include <stdio.h>
#define METER_CONVERSION 0.09290304

int main(void) {
    float length, width, area;
    printf("What is the length of the room in feet? ");
    scanf("%f", &length);
    printf("What is the width of the room in feet? ");
    scanf("%f", &width);
    area = length * width;
    printf("The area is\n");
    printf("%.0f square feet\n", area);
    printf("%.3f square meters\n", METER_CONVERSION * area);
    return 0;
}
