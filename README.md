# TimeTable

The TimeTable repository is a system that facilitates the scheduling of classes for teachers and supervisors. It distinguishes between two types of users: teachers and supervisors, each with their respective APIs for registration. The users are differentiated by two boolean attributes: `is_teacher` and `is_supervisor`.

## User Types

1. **Teachers**: Teachers are individuals who offer their availability to conduct classes. They have the following API for registration:
   - `/api/register_teacher`: Endpoint for teacher registration.

2. **Supervisors**: Supervisors are responsible for managing the scheduling of classes. They have the following API for registration:
   - `/api/register_supervisor`: Endpoint for supervisor registration.

Once registered, supervisors can set the `teacher_id` for each teacher using the following API:
- `/api/set_teacher_id`: API to set the `teacher_id` for a teacher.

## Time Sections

The TimeTable system consists of two main types of timetables.

### 1. Free Time Sections Table

Time sections are the blocks of time during which a teacher is available to conduct classes. These sections are defined for each teacher and can be utilized by supervisors to schedule classes. The time sections are scheduled every day of the week and occur every 45 minutes, starting from 9:00 - 9:45 and continuing until 21:00 - 21:45.

#### Class Model

The class model includes the following fields:
- `student`: Represents the student enrolled in the class.
- `platform`: Indicates the platform where the class will be conducted.
- `session`: Specifies additional session details.

### 2. Main Timetable

The main timetable is a comprehensive view accessible to supervisors, displaying the scheduled classes for each teacher. It allows supervisors to quickly see which teachers are teaching during a specific time section or which teachers have free time during a particular period.

---

By following these guidelines, the TimeTable project becomes an efficient tool for managing class schedules and facilitating communication between teachers and supervisors. With its user-friendly APIs and clear organization of time sections, the project aims to streamline the scheduling process and enhance the overall teaching experience.
