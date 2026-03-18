# DUDataflowAnomalyAnalysis Rule

As per the **DUDataflowAnomalyAnalysisRule**, the rule analyzes the **data flow of variables**, not just whether they appear to be used in the code.

The rule flags a variable when all of the following conditions are met:

* The variable is defined.
* It later goes out of scope (becomes undefined) when the method exits.
* There exists at least one valid execution path where the variable is never referenced.

A **reference** means an actual read or method call on the variable (for example, accessing a property or invoking a method).

**Return statements are not treated as references by this rule.**

There is also a possibility of violation if the method exits before reaching the variable usage due to an **exception statement**.

The **DUDataflowAnomalyAnalysis rule** analyzes the data flow of local variables throughout a method. It does not just look at the code as a whole; it traces **every possible execution path through the method individually**. It flags a violation when a variable is defined but there exists at least one execution path where it is never read or used before the method exits. Even if a variable is used on one path, if there is even one path where it is never touched, the rule will flag it.

**Expected Behavior**

The **DUDataflowAnomalyAnalysis rule** performs **path-sensitive dataflow analysis** and evaluates every possible execution path in a method. If there is any path where the variable is defined but never read before the method exits, the rule will raise a violation, even if it is used in other branches.

If the goal is to detect variables that are simply never used, the **UnusedLocalVariable rule** may better fit the requirement. Otherwise, the issue can be **marked as a False Positive if the behavior is expected**.
