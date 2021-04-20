using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using EasyEats.FitTrekWebService;
using EasyEats.FitTrekWebApp;

namespace FitTrek.WorkoutSearch
{
    public class InterpreterContext
    {
        private WorkoutId workoutId;

        public InterpreterContext(String endpoint)
        {
            workoutId = new WorkoutId(endpoint);
        }

        public List<WorkoutInformation> GetAllWorkouts()
        {
            return workoutId.GetAllWorkouts;
        }
    }
}
