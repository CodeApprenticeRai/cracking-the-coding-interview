using System;
using System.Collections.Generic;

namespace IsUnique
{
    class IsUnique
    {
        static void Main()
        {
            Console.Write("Enter a word to analyze: ");
            string word = Console.ReadLine();

            HashSet<char> cache = new HashSet<char>(word);

            if (cache.Count != word.Length)
            {
                Console.WriteLine("The string entered does not consist of unique characters.");
            } else {
                Console.WriteLine("The string entered consists of unique characters.");
            }
            Console.ReadKey();
        }
    }
}