using FitTrek.FitTrekWebApp;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FitTrek.Tracking
{
    public class Customers : ICustomers
    {
        private CustomerInformation CustomerInformation;
        private Workout workout;
        public Workout Workout
        {
            get { return workout; }
            set { workout = value; }
        }
        public Customers(CustomerInformation CustomerInformation)
        {
            this.CustomerInformation = CustomerInformation;
        }
        public void Update(Exercise exercise)
        {
            Console.WriteLine("Notified Workout ID {0} of Order ID {1}'s Workout Status: {2}", exercise.WorkoutId,
                exercise.WorkoutId, exercise.workoutconfirmation);
            Console.WriteLine("Date Time: {0}", exercise.completedtime);
        }
    }
}
