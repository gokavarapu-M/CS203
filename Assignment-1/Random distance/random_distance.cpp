#define _USE_MATH_DEFINES

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <math.h>

#define max RAND_MAX
#define pi M_PI
using namespace std;

double RandomDistance(double radius)
{
    return (((double)rand() / max) *
            radius); // Generates a random distance from the center
}

double ChordLength(double radius, double distance)
{
    return (
        2 *
        sqrt(pow(radius, 2) -
             pow(distance, 2))); // Calculates the length of the chord given the perpendicular distance
}

int main()
{

    srand(time(NULL)); // Seed the random number generator with current time

    double radius;
    cout << "Enter the radius of the circle: ";
    cin >> radius;

    int num_simulations;
    cout << "Enter the number of simulations: ";
    cin >> num_simulations;

    double length =
        sqrt(3) *
        radius;   // side length of the equilateral triangle for given radius
    double a = 0; // to count no.of chords with length greater than  side length
                  // of the triangle
    double b = 0; // to count no.of chords with length less than or equal to  side
                  // length of the triangle

    for (int i = 0; i < num_simulations; ++i)
    {
        double distance = RandomDistance(radius);
        double chord_length = ChordLength(radius, distance);
        if (chord_length > length)
        {
            a++;
        }
        else
        {
            b++;
        }
    }

    double event; // the probability of chords with length greater than  side
                  // length of the triangle
    event = a / (a + b);
    cout << "Probablility of the event is: " << event << endl;

    return 0;
}