using FitTrek.FitTrekWebApp;
using FitTrek.WorkoutSearch;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FitTrek.WorkoutId
{
    public abstract class AbstractExpression
    {
        public abstract List<WorkoutInformation> Interpret(InterpreterContext context);
    }
}