using System;

namespace Degree {
    class Program {
            static void Main(string[] args) {
                double n = Convert.ToDouble(Console.ReadLine());

                double tmp = n * n;     // n ^ 2
                n = tmp * tmp;          // n ^ 4
                n = n * tmp;            // n ^ 6
                n = tmp * tmp * n;      // n ^ 10

            Console.WriteLine($"{n:f3}");
        }
    }
}