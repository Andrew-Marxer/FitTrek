using FitTrek.FitTrekWebApp;
using FitTrek.WorkoutList;
using FitTrek.WorkoutWebService;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FitTrek.TheList
{
    public class WorkoutList : IWorkoutList
    {
        private string WorkoutID;
        public WorkoutList(string WorkoutID)
        {
            this.WorkoutID = WorkoutID;
        }
        public List<WorkoutInformation> GetWorkoutInfo()
        {
            WorkoutListServices workoutListServices = new WorkoutListServices(string.Empty, WorkoutID);
           var workoutListItems = workoutListServices.getAllWorkouts(WorkoutID);

            return workoutListItems;
        }
        public IIterator CreateFoodMenuIterator()
        {
            var workoutListItems = GetWorkoutInfo();
            return new WorkoutListIterator(workoutListItems);
        }
    }
}
