using System;
using System.Collections.Generic;

namespace ExamenParcial_2_JCAT
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<char> numeros = new List<char> { '1', '2', '3', '4', '5', '6', '7', '8', '9', '0' };
            List<char> caracteres = new List<char> { '.', '@', '#' };
            List<char> letras = new List<char> { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
            string placa = "";
            int contador = 0;
            Console.Write("Introduzca su placa: ");
            placa = Console.ReadLine();
            placa = placa.ToUpper();
            if(placa.Length <= 8) //Validando si tiene mas de 8 digitos
            {
                if (VerificaCaracterValido(placa) && VerificaDigitoNumericos(placa) && VerificarCaracteres(placa)) //Validacion con los metodos desarrollados
                {
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine($"La placa {placa} es valido en el territorio Boliviano");
                    Console.ForegroundColor = ConsoleColor.White;
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"La placa {placa} no es valido en el territorio Boliviano");
                    Console.ForegroundColor = ConsoleColor.White;
                }
            }
            else
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine($"La placa {placa} no es valido en el territorio Boliviano");
                Console.ForegroundColor = ConsoleColor.White;
            }



            //Metodo que verifica si los 3 o 4 digitos son numeros
            bool VerificaDigitoNumericos(string placa)
            {
                contador = 0;
                for (int i = 0; i < 4; i++)
                {
                    if (numeros.Contains(placa[i]))//Verificando si son numeros comparando con nuestra lista de numeros
                        contador++;
                }
                return contador > 2 && contador < 5 ? true : false; //asignacion con el operador ternario Verificando la validacion
            }

            //Metodo que verifica si los ultimos 3 digitos son letras
            bool VerificarCaracteres(string placa)
            {
                contador = 0;
                for (int i = placa.Length-1; i > placa.Length-4; i--)
                {
                    if (letras.Contains(placa[i]))
                        contador++;
                }
                return contador == 3 ? true : false; //asignacion con el operador ternario Verificando la validacion
            }

            //Metodo que verifica si contiene caracteres como ('.','@','#') si contiene nos devuele un false 
            bool VerificaCaracterValido(string placa)
            {
                contador = 0;
                foreach (char caracter in placa)
                {
                    if (caracteres.Contains(caracter))
                        contador++;
                }
                return contador == 0 ? true : false; //asignacion con el operador ternario Verificando la validacion
            }
        }
    }
}
