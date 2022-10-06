using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class PolloSpiedo : ComidaRapidaComponente
    {
        public override double Costo
        {
            get { return 50; }
        }

        public override string Descripcion
        {
            get { return $"\n{Costo}bs.\tPollo Entero al Spiedo"; }
        }
    }
}
