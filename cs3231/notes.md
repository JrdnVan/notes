# COMP3231 Notes

# Table Content

# Overview of Operating Systems

# Processes and Threads

# Concurrency and Synchronisation
## Race Conditions
e.g. Imagine the global variable count being shared between two threads.

    void inc(){
        int t = count; 
        t = t + 1; 
        count = t;
    }

    void dec(){
        int t = count; 
        t = t - 1; 
        count = t;
    }

After both increment and decrement functions are called at the same time, the resulting count doesn't equal 0 due to the race condition.
- Count would equal 1 or -1.

## Critical Regions
Critical regions are regions of the code that access shared recourses.
- e.g. Global variables  

Correctness would rely on shared resources not being concurrently modified by another thread or process.  
Uncoordinated entry to the critical region results in the race condition.  
- Incorrect behaviour, deadlock, etc.
### Example of Mutual Exclusion using Critical Region
Two processes, A and B.  

    A enters critical region.
    B attempts to enter critical region as A is still in the middle of computing.
    B gets blocked from entering.
    A leaves the critical region.
    B can now enter the critical region.
    B leaves the critical region.

### Solutions to the Critical Region problem
We need to fulfill all the below conditions to solve any critical region problem.
- Mutual Exclusion:
  - No two processes simultaneously inside critical region.
- No assumptions made about speeds or numbers of CPU.
- Progress:
  - No process running outside its critical region may block another process.
- Bounded:
  - No process waits forever to enter critical region.

## Semaphores
Dijkstra(1965) introduced two primitives more powerful than the simple sleep and wakeup alone.  

    P(); //probergen, from Dutch to test, AKA wait.
    V(); //verhogen, from Dutch to increment, AKA signal.

Both functions are executed atomically.
  - No race condition.
  - Disabled interrupts.

Usages: 

    struct semaphore *sem_create(const char *name, int initial_count);
    void sem_destroy(struct semaphore *);
    void P(struct semaphore *);
    void V(struct semaphore *);

Summary:
  - Can be used to solve a variety of concurrency problems.
  - Programming with semaphores can be error-prone.
    - e.g. Must signal for every wait for mutexes.
      - Too many or too few signals/waits(Or in wrong orders) can have catastrophic results.
### How do semaphores work?
- If resource unavailable, corresponding semaphore blocks any process waiting for the resource.
- Blocked processes are put into a process queue maintained by semaphore.
- When process releases a resource, it signals to semaphore it's done.
- Signalling resumes a blocked process
- Wait and signal operations can't be interrupted.

### Semaphore Implementation
...

### Semaphore Implementation of a Mutex
Mutex is short for Mutual Exclusion.
  - Also called a lock.
    - Usages:

            //Functions to create and destroy locks
            struct lock *lock_create(const char *name);
            void lock_destroy(struct lock *);

            //Functions to acquire and release them
            void lock_acquire(struct lock *);
            void lock_release(struct lock *);

Example code below:

    semaphore mutex; 
    mutex.count = 1; //initialise mutex  
    wait(mutex); //enter the critcal region   
    Blahblah();  
    signal(mutex); //exit the critical region    

## Monitors
Hoare(1974) proposed monitors to ease concurrent programming.
  - Higher level synchronisation primitive.
  - Programming language construct.

Idea: 
  - Set of procedures, variables, data types are grouped in a special kind of module, the monitor.
    - Variables and data types only accessed from within monitor.
  - Only one process/thread can be in the monitor at any one time.
    - Mutual exclusion is implemented by the compiler.
      - Less error prone.
  - When a thread calls a monitor procedure that has a thread inside it already, it is queued and slept until the current thread exits monitor.

## Condition Variables
To allow a process to wait within a monitor, condition variables must be declared as:

    condition x, y;

Usages:

    struct cv *cv_create(const char *name);
    void cv_destroy(struct cv *);

    void cv_wait(struct cv *cv, struct lock *lock);
    void cv_signal(struct cv *cv, struct lock *lock);
    void cv_broadcast(struct cv *cv, struct lock *lock);

Condition variables can only be used with the operations wait and signal.

    x.wait();
    x.signal();

- Wait:
  - Means process invoking the operation is suspended until another process invokes.
  - Another thread can enter monitor while original is suspended.
- Signal:
  - Resumes a suspended process. 
    - If no process suspended, signal has no effect.


# Deadlocks

# Processes and Threads Implementation

# System Calls and R3000 Overview

## System Calls
System Calls can be viewed as a special function call.
- Provides for a controlled entry into the kernel.
- While in kernel, perform privileged operation.
- Returns to original caller the result.

From the user's perspective:
- Process Management
- File I/O
- Directories Management
- Some other selected calls

### System Calls for Process Management
Process Management:  

    pid = fork() //Creates child process identical to parent.
    pid = waitpid(pid, &statloc, options) //Wait for child to terminate.
    s = execve(name, argv, environp) //Replace a process' core image.
    exit(status) //Terminate process execution and return status.

### System Calls for File Management

### System Call Implementation
i.e. Crossing the user-kernel boundary.
- ### A Simple Model of CPU Computation
  
- ### Privileged-mode Operation

### MIPS R300
- ### Coprocessor 0
  - ### Introduction
    Process Control registers are locating in Coprocessor 0 (CP0).
      - Exception/Interrupt management registers
      - Translation management registers  
    
    CP0 is manipulated using move to(MTC0) and move from(MFC0) instructions.
      - MTC0/MFC0 are only accessible in kernel mode.

  - ### Coprocesser 0 Registers
    Exception Management:  
    /////////////////TODO//
  - ### C0_STATUS
    Bits: 

        KU ? user mode : kernel  
        IE ? interrupts enabled : all interrupts masked  
        c, p, o = current, previous, old

  - ### C0_CAUSE

  - ### C0_EPC
    The Exception Program Counter
    - Points to address of where to restart execution after handling the exception or interrupt.

# Computer Hardware Review

## Operating System
  - Exploit hardward available
  - Provide set of high level services that represent or are implemented by hardware.
  - ...TODO

## Caching as a general technique

  - Two levels of data storage: small and fast, versus large and slow.
  - Can speed access to slower storage by using intermediate-speed storage as a cache.

