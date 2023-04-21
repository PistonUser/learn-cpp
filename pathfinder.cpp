#include <iostream>
#include <string>
#include <fstream>
#include <cmath>
using namespace std;

int main() {
	int points[3][2] =
    {
        {1,4}, {2,2}, {4,3}
    };

    for (int i = 0; i < sizeof(points) / sizeof(int) / 2; i++) {
        for (int a = 0; a < sizeof(points) / sizeof(int) / 2; i++) {
            float b = hypot(points[i][0] - points[a][0] ,points[i][1] - points[a][1]);

    }
}