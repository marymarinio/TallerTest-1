using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class Gaseosa : AgregadoDecorador
    {
        private Tamanio _tamanio;
        private TipoGaseosa _gaseosa;
        public Gaseosa(ComidaRapidaComponente comida, Tamanio tam, TipoGaseosa gaseosa) : base(comida)
        {
            this._tamanio = tam;
            this._gaseosa = gaseosa;
        }

        public override double Costo
        {
            get
            {
                return base._comidaRapida.Costo + ((_tamanio == Tamanio.Pequeño) ? 8 :
                               (_tamanio == Tamanio.Mediano) ? 10 : 13);
            }
        }

        public override string Descripcion
        {
            get
            {
                return base._comidaRapida.Descripcion + $"\n{((_tamanio == Tamanio.Pequeño) ? 8 : (_tamanio == Tamanio.Mediano) ? 10 : 13)}bs.\tGaseosa {_gaseosa} {_tamanio}";
            }
        }
    }
}
