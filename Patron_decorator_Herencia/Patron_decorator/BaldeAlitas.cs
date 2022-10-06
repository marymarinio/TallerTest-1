using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class BaldeAlitas : ComidaRapidaComponente
    {
        public override double Costo
        {
            get { return 25.50; }
        }

        public override string Descripcion
        {
            get { return $"\n{Costo}bs.\t Balde Alitas"; }
        }
    }
}
