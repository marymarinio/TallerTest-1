using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class PolloBroaster : ComidaRapidaComponente
    {
        public override double Costo
        {
            get { return 40; }
        }

        public override string Descripcion
        {
            get { return $"\n{Costo}bs.\tPollo Entero Broaster"; }
        }
    }
}
