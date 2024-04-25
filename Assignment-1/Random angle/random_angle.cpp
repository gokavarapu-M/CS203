#define _USE_MATH_DEFINES

#include <math.h>
#include <cstdlib>
#include <ctime>
#include <iostream>

#define max RAND_MAX
#define pi M_PI
using namespace std;

double RandomAngle()
{
  return (((double)rand() / max) *
          pi); // Generates a random angle in radians
}

double ChordLength(double radius, double angle)
{
  return (2 * radius *
          sin(angle / 2)); // Calculates the length of the chord given the angle
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
    double angle = RandomAngle();
    double chord_length = ChordLength(radius, angle);
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
