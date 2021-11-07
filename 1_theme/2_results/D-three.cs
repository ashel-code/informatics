using System;

namespace Degree {
    class Program {
        static void Main(string[] args) { 
            int n = Convert.ToInt32(Console.ReadLine());

            if(n >= 1000 || n < 100)
            {
                Console.WriteLine("NO");
            }
            else
            {
                Console.WriteLine("YES");
            }

            Console.ReadLine();
        }
    }
}