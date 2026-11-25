---
created: 2026-11-25T13:20
updated: 2026-11-25T13:21
---

---

Here is my vision of the repo and the workflow. This relates, refine, and complement to my approval of draft no 2. Create a separated draft for me to review, about: you expand on this further if you can. Correct my vision, identify the gaps, deadlocks, tighten, close the cycle, refactor by trimming down redundancy, optimize your workflow, step-by-step. 

- /archive: trash can with retention policy 
- /[area]: an area of interest. For example, right now the repo has /novels, where I explore writing novels 
	- /resources: acts as permanent archive for the are of interest. see /workspace/[project-id] below 
- /workspace: a working session 
	- chat.md: 3 sections 
		- current: brief what you're doing with a link to the task you're doing 
		- open discussion: this is to combat my limited context of a chat window; conversations that haven't finalized into a draft go here. You must log our conversation exactly word-by-word, respecting .md format. This means when I post comment you must log it in here, when you reply you must log it in here. When we got a draft from that conversation then you clear our talk prior to it, put a link the draft instead, then move on logging conversation form there. Repeat the cycle when the draft got updated or revised. You and me both can start a conversation, not just me. 
		- reports: 3 most recent reports, newest one at the top, delete the old ones
	- /misc: things that don't fit in any project. They might or might not be classified/promoted to relocate to their appropriate places in projects, waiting for my decisions. Create a workspace task, open a conversation in open discussion section in discussion.md, link the task in it, then remind me 
	- /task: contains workspace tasks that don't fit in any project. These tasks are supposed to be lightweight, so no ADR, no draft. If there is then ask me to start a project, and move the tasks in properly 
		- /[task-id] 
			- TASK.md  
			- PROGRESS.md: task progress 
			- PLAN.md: task plan 
	- /project: contains multiple ongoing projects. A project is a working session of an area of interest. We can have multiple ongoing projects in an area 
		- /[project-id]: id should have prefixes respecting its area. When the project is completed, move this entire folder to root /archive. The retention policy is of the entire project folder: 90 days
			- PLAN.md: project plan 
			- PROGRESS.md: project progress 
			- TASK_BOARD.md: project tasks board
			- /task: tasks don't have their own resources. What they found will be put into project /resources and can be used project-wide
				- /[task-id]: id should have prefixes respecting its area and its project 
					- TASK.md  
					- PROGRESS.md: task progress. Update project progress briefly accordingly. If you want to see details then read this file.
					- PLAN.md: task plan. Update project plan briefly accordingly. If you want to see details then read this file.
			- /draft: project drafts. Throwaway drafts are moved to the project /archive/drafts. When I approve a draft, it is promoted to an ADR and moved to the project /resource/adr. When a decision  need to be revised and updated, create a new draft instead of direct modification in an ADR. Repeat the cycle. This means an ADR is immutable, they represent decisions in chronological order. 
			- /resource: ADRs, references, findings, etc. that benefit the whole project go here. These will be moved to the root /[area]/resources when the project is completed. Throw away resources are moved to the project /archive/resources 
				- /adr: ADRs of the project 
				- /reference: references of the project 
				- /finding: findings of the project 
				- /misc: things that don't fit in any folder but worth keeping in the project scope 
			- /archive: the archive of the project 
				- /task: completed task 
				- /draft: throwaway drafts 
				- /resources: matches exactly as the project /resources 
					- /adr: throwaway ADRs  
					- /reference: throwaway references  
					- /finding: throwaway findings 
					- /misc: throwaway things 

---

