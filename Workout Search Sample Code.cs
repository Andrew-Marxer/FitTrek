using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkoutSearch, Workouts
{
	public class WorkoutSearchClient
	{
		Private WorkoutInterpreterContext context;
		public WorkoutSearchClient(WorkoutInterpreterContext context)
		{
			this.context = context;
		}
		
		public List<WorkoutInformation> Inercept(string expression)
		{
            AbstractExpression queryExpression = null;
            String[] stringParts = expression.Split(' ');
            String searchType = stringParts[0];
            String searchAttribute = stringParts[2];

            var startIndex = expression.IndexOf("'");
            var lastIndex = expression.LastIndexOf("'");
            var length = expression.Length;
            String query = expression.Substring(startIndex+1, lastIndex - startIndex-1);

            if (searchType.Equals("workout") && searchAttribute.Equals("calories"))
                queryExpression = new WorkoutProcedure(query);

            if (queryExpression != null)
                return queryExpression.Interpret(this.context);

            return null;
		}
	}
}