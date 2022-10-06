using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Patron_decorator
{
    public class Postre : AgregadoDecorador
    {
        private Sabor _sabor;

        public Postre(ComidaRapidaComponente comida, Sabor sabor) : base(comida)
        {
            this._sabor = sabor;
        }

        public override double Costo
        {
            get
            {
                return base._comidaRapida.Costo + 7;
            }
        }

        public override string Descripcion
        {
            get
            {
                return base._comidaRapida.Descripcion + $"\n{7}bs.\tPostre Pie {_sabor}";
            }
        }
    }
}
