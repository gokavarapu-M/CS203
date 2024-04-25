#define _USE_MATH_DEFINES

#include <cstdlib>
#include <ctime>
#include <iostream>
#include <math.h>

#define max RAND_MAX
#define pi M_PI
using namespace std;

double RandomAngle()
{
    return (((double)rand() / max) * 2 *
            pi); // Generates a random angle in radians
}

double RandomDistance(double radius)
{
    return (((double)rand() / max) * 2 *
            radius); // Generates a random distance from the center
}

double ChordLength(double radius, double X, double Y)
{
    double distance =
        sqrt(pow(X, 2) + pow(Y, 2)); // distance for point from center of circle

    return (2 * sqrt(pow(radius, 2) -
                     pow(distance, 2))); // Calculates the length of the chord
                                         // given the perpendicular distance
}
// Calculates the length of the chord given the midpoint of chord

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
        double angle = RandomAngle();
        double dist = RandomDistance(radius);
        double X = dist * sin(angle);
        double Y = dist * cos(angle);
        double chord_length = ChordLength(radius, X, Y);
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
