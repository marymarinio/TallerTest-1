using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class PapasFritas : AgregadoDecorador
    {
        private Tamanio _tamanio;
        public PapasFritas(ComidaRapidaComponente comida, Tamanio tam) : base(comida)
        {
            this._tamanio = tam;
        }

        public override double Costo
        {
            get {
                return base._comidaRapida.Costo + ((_tamanio == Tamanio.Pequeño) ? 7.5 :
                               (_tamanio == Tamanio.Mediano) ? 9.5 : 11.5);
            }
        }

        public override string Descripcion
        {
            get
            {
                return base._comidaRapida.Descripcion + $"\n{((_tamanio == Tamanio.Pequeño) ? 7.5 :(_tamanio == Tamanio.Mediano) ? 9.5 : 11.5)}bs.\tPapas Fritas {_tamanio}";
            }
        }
    }
}
