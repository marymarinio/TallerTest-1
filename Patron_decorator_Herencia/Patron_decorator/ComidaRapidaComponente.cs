using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public abstract class ComidaRapidaComponente
    {
        public abstract double Costo { get; }
        public abstract string Descripcion { get; }
    }
}
