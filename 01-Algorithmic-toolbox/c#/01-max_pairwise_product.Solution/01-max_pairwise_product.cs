using System;

namespace MaxPairwiseProblem
{
    public class Program
    {
        static void Main()
        {
            Console.WriteLine("Welcome to Max pairwise product program");
            int n;
            while (true)
            {
                try 
                {
                    Console.WriteLine("Enter n:");
                    n = int.Parse(Console.ReadLine());
                    break;
                }
                catch
                {
                    Console.WriteLine("Not a number");
                }
            }

            int[] numbers = new int[n]; 
            while (true)
            {
                try 
                {
                    Console.WriteLine("Enter numbers");
                    numbers = Array.ConvertAll(Console.ReadLine().Split(" "), s => int.Parse(s));
                    break;
                }
                catch
                {
                    Console.WriteLine("Not in correct format : 0 1 2 3 4");
                }
            }
            Console.WriteLine("Max pairwise product is " + GetMaxPairwiseProblem(numbers));
        }

        static int GetMaxPairwiseProblem(int[] numbers)
        {
            if (numbers.Length < 1)
            {
                return -1;
            }
            else if (numbers.Length == 1)
            {
                return numbers[0];
            }
            else if (numbers.Length == 2)
            {
                return numbers[0] * numbers[1];
            }

            int max1 = numbers[0] > numbers[1] ? numbers[0] : numbers[1];
            int max2 = numbers[0] > numbers[1] ? numbers[1] : numbers[0];

            for (int i = 2; i < numbers.Length; i++)
            {
                if (numbers[i] > max1)
                {
                    max2 = max1;
                    max1 = numbers[i];
                }
                else if (numbers[i] > max2)
                {
                    max2 = numbers[i];
                }
            }
            return max1 * max2;
        }
    }
}