using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class Arroz : AgregadoDecorador
    {
        private Tamanio _tamanio;
        public Arroz(ComidaRapidaComponente comida, Tamanio tam) : base(comida)
        {
            this._tamanio = tam;
        }

        public override double Costo
        {
            get
            {
                return base._comidaRapida.Costo + ((_tamanio == Tamanio.Pequeño) ? 6 :
                               (_tamanio == Tamanio.Mediano) ? 8 : 18);
            }
        }

        public override string Descripcion
        {
            get
            {
                return base._comidaRapida.Descripcion + $"\n{((_tamanio == Tamanio.Pequeño) ? 6 : (_tamanio == Tamanio.Mediano) ? 8 : 18)}bs.\tArroz {_tamanio}";
            }
        }
    }
}
