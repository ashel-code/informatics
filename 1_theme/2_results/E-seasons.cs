using System;

namespace Degree {
    class Program {
        static void Main(string[] args) { 
            int n = Convert.ToInt32(Console.ReadLine());

            if(n > 0 && n <= 12) 
            {
                if(n <= 2 || n == 12)
                {
                    Console.WriteLine("winter");
                }
                else if(n <= 5)
                {
                    Console.WriteLine("spring");
                }
                else if(n <= 8)
                {
                    Console.WriteLine("summer");
                }
                else 
                {
                    Console.WriteLine("autumn");
                }
            }
            else
            {
                Console.WriteLine("NO");
            }

            Console.ReadLine();
        }
    }
}