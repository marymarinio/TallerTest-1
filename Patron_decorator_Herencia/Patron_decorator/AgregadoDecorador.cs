using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public abstract class AgregadoDecorador : ComidaRapidaComponente
    {
        protected ComidaRapidaComponente _comidaRapida;
        public AgregadoDecorador(ComidaRapidaComponente comida)
        {
            this._comidaRapida = comida;
        }
    }
}
