from django.core.management.base import BaseCommand
from learning.models import Technology, Roadmap, Topic


TECHNOLOGIES = [
    {
        'name': 'Python',
        'description': 'A powerful, beginner-friendly programming language used in web development, AI, data science, and automation.',
        'icon': 'python',
        'color': 'warning',
        'order': 1,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'Python Fundamentals',
                'description': 'Learn Python basics: syntax, variables, control flow, and functions.',
                'order': 1,
                'topics': [
                    {
                        'name': 'Variables & Data Types',
                        'explanation': 'Variables store data values. Python has no command for declaring a variable — it is created when you first assign a value. Common data types include int, float, str, bool, list, dict, tuple.',
                        'example': 'name = "Alice"\nage = 25\nheight = 5.7\nis_student = True\nprint(f"Hello, {name}! You are {age} years old.")',
                        'learning_objective': 'Understand how to create variables, assign values, and work with Python\'s built-in data types.',
                        'order': 1,
                    },
                    {
                        'name': 'Control Flow (if/else)',
                        'explanation': 'Control flow statements allow your program to make decisions. if/elif/else lets you execute code based on conditions.',
                        'example': 'score = 85\nif score >= 90:\n    print("Grade: A")\nelif score >= 80:\n    print("Grade: B")\nelse:\n    print("Grade: C")',
                        'learning_objective': 'Write conditional logic using if, elif, and else statements to control program execution.',
                        'order': 2,
                    },
                    {
                        'name': 'Loops (for & while)',
                        'explanation': 'Loops allow you to repeat a block of code. for loops iterate over sequences; while loops run while a condition is true.',
                        'example': 'fruits = ["apple", "banana", "cherry"]\nfor fruit in fruits:\n    print(fruit)\n\ncount = 0\nwhile count < 3:\n    print(count)\n    count += 1',
                        'learning_objective': 'Use for and while loops to iterate over data and repeat operations efficiently.',
                        'order': 3,
                    },
                    {
                        'name': 'Functions',
                        'explanation': 'Functions are reusable blocks of code that perform a specific task. They help organize code and avoid repetition.',
                        'example': 'def greet(name, greeting="Hello"):\n    return f"{greeting}, {name}!"\n\nresult = greet("Bob")\nprint(result)  # Hello, Bob!\nprint(greet("Alice", "Hi"))',
                        'learning_objective': 'Define and call functions with parameters and return values to create reusable code.',
                        'order': 4,
                    },
                    {
                        'name': 'Lists & Dictionaries',
                        'explanation': 'Lists store ordered collections of items. Dictionaries store key-value pairs for fast lookups.',
                        'example': 'my_list = [1, 2, 3, 4, 5]\nmy_list.append(6)\nprint(my_list[0])  # 1\n\nstudent = {"name": "Alice", "grade": "A", "age": 20}\nprint(student["name"])',
                        'learning_objective': 'Create, access, modify, and iterate over lists and dictionaries to manage collections of data.',
                        'order': 5,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'Object-Oriented Python',
                'description': 'Learn OOP concepts: classes, inheritance, encapsulation, and polymorphism.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Classes & Objects',
                        'explanation': 'A class is a blueprint for creating objects. Objects are instances of classes that have attributes (data) and methods (functions).',
                        'example': 'class Car:\n    def __init__(self, brand, model):\n        self.brand = brand\n        self.model = model\n    \n    def describe(self):\n        return f"{self.brand} {self.model}"\n\nmy_car = Car("Toyota", "Corolla")\nprint(my_car.describe())',
                        'learning_objective': 'Create classes with attributes and methods, and instantiate objects from those classes.',
                        'order': 1,
                    },
                    {
                        'name': 'Inheritance',
                        'explanation': 'Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.',
                        'example': 'class Animal:\n    def speak(self):\n        pass\n\nclass Dog(Animal):\n    def speak(self):\n        return "Woof!"\n\nclass Cat(Animal):\n    def speak(self):\n        return "Meow!"\n\ndog = Dog()\nprint(dog.speak())  # Woof!',
                        'learning_objective': 'Use inheritance to create specialized classes that extend parent class behavior.',
                        'order': 2,
                    },
                    {
                        'name': 'Decorators & Context Managers',
                        'explanation': 'Decorators modify functions without changing their code. Context managers handle setup and teardown automatically (e.g., file handling).',
                        'example': 'def timer(func):\n    import time\n    def wrapper(*args):\n        start = time.time()\n        result = func(*args)\n        print(f"Took {time.time()-start:.2f}s")\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    import time; time.sleep(1)',
                        'learning_objective': 'Apply decorators to enhance functions and use context managers for resource management.',
                        'order': 3,
                    },
                    {
                        'name': 'Error Handling',
                        'explanation': 'Exception handling with try/except prevents programs from crashing due to unexpected errors.',
                        'example': 'def divide(a, b):\n    try:\n        result = a / b\n        return result\n    except ZeroDivisionError:\n        return "Cannot divide by zero!"\n    except TypeError as e:\n        return f"Type error: {e}"\n    finally:\n        print("Operation complete")',
                        'learning_objective': 'Implement robust error handling to create programs that gracefully handle unexpected situations.',
                        'order': 4,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Advanced Python',
                'description': 'Master generators, async programming, metaclasses, and performance optimization.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Generators & Iterators',
                        'explanation': 'Generators produce values lazily using the yield keyword, making them memory-efficient for large datasets.',
                        'example': 'def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\nfib = fibonacci()\nfor _ in range(10):\n    print(next(fib))',
                        'learning_objective': 'Create generator functions and custom iterators for memory-efficient data processing.',
                        'order': 1,
                    },
                    {
                        'name': 'Async/Await Programming',
                        'explanation': 'Asynchronous programming with asyncio allows concurrent execution without threads, ideal for I/O-bound operations.',
                        'example': 'import asyncio\n\nasync def fetch_data(url):\n    await asyncio.sleep(1)  # Simulates network request\n    return f"Data from {url}"\n\nasync def main():\n    tasks = [fetch_data(f"url_{i}") for i in range(3)]\n    results = await asyncio.gather(*tasks)\n    print(results)\n\nasyncio.run(main())',
                        'learning_objective': 'Write asynchronous Python code using async/await to handle concurrent I/O operations efficiently.',
                        'order': 2,
                    },
                    {
                        'name': 'Metaclasses & Descriptors',
                        'explanation': 'Metaclasses are the "class of a class" — they control how classes are created. Descriptors control attribute access behavior.',
                        'example': 'class SingletonMeta(type):\n    _instances = {}\n    def __call__(cls, *args, **kwargs):\n        if cls not in cls._instances:\n            cls._instances[cls] = super().__call__(*args, **kwargs)\n        return cls._instances[cls]\n\nclass Database(metaclass=SingletonMeta):\n    pass',
                        'learning_objective': 'Understand metaclass programming and descriptor protocol to control class creation and attribute access.',
                        'order': 3,
                    },
                ]
            },
        ]
    },
    {
        'name': 'JavaScript',
        'description': 'The language of the web — used for interactive frontends, Node.js backends, and full-stack development.',
        'icon': 'js',
        'color': 'warning',
        'order': 2,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'JS Fundamentals',
                'description': 'Learn JavaScript basics: variables, functions, DOM manipulation.',
                'order': 1,
                'topics': [
                    {
                        'name': 'Variables & Scope',
                        'explanation': 'JavaScript has three ways to declare variables: var, let, and const. let and const use block scope, while var uses function scope.',
                        'example': 'const name = "Alice";\nlet age = 25;\nvar city = "New York";\n\nconst greet = () => {\n    const message = `Hello, ${name}!`;\n    return message;\n};\nconsole.log(greet());',
                        'learning_objective': 'Understand variable declarations with var/let/const and how JavaScript scoping rules work.',
                        'order': 1,
                    },
                    {
                        'name': 'DOM Manipulation',
                        'explanation': 'The DOM (Document Object Model) is a tree of HTML elements. JavaScript can access, modify, add, and remove DOM elements dynamically.',
                        'example': 'const button = document.getElementById("myBtn");\nbutton.addEventListener("click", function() {\n    const para = document.createElement("p");\n    para.textContent = "Button clicked!";\n    document.body.appendChild(para);\n});',
                        'learning_objective': 'Select, modify, create, and delete HTML elements using the DOM API to create dynamic web pages.',
                        'order': 2,
                    },
                    {
                        'name': 'Arrays & Array Methods',
                        'explanation': 'JavaScript arrays have powerful built-in methods like map, filter, reduce, find, and forEach for transforming data.',
                        'example': 'const numbers = [1, 2, 3, 4, 5];\nconst doubled = numbers.map(n => n * 2);\nconst evens = numbers.filter(n => n % 2 === 0);\nconst sum = numbers.reduce((acc, n) => acc + n, 0);\nconsole.log(doubled, evens, sum);',
                        'learning_objective': 'Use JavaScript array methods (map, filter, reduce, etc.) to transform and process collections of data.',
                        'order': 3,
                    },
                    {
                        'name': 'Fetch API & Promises',
                        'explanation': 'The Fetch API makes HTTP requests and returns Promises. async/await syntax makes asynchronous code readable.',
                        'example': 'async function getData(url) {\n    try {\n        const response = await fetch(url);\n        const data = await response.json();\n        return data;\n    } catch (error) {\n        console.error("Error:", error);\n    }\n}\n\ngetData("https://api.example.com/users").then(console.log);',
                        'learning_objective': 'Make HTTP requests using the Fetch API and handle asynchronous operations with Promises and async/await.',
                        'order': 4,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'Modern JavaScript',
                'description': 'ES6+, closures, prototypes, and functional programming.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Closures & Scope',
                        'explanation': 'A closure is a function that retains access to its outer scope even after the outer function has returned. This enables powerful patterns like data privacy.',
                        'example': 'function createCounter() {\n    let count = 0;\n    return {\n        increment() { count++; },\n        decrement() { count--; },\n        getCount() { return count; }\n    };\n}\nconst counter = createCounter();\ncounter.increment();\nconsole.log(counter.getCount()); // 1',
                        'learning_objective': 'Understand closure mechanics and use closures to create private state and factory functions.',
                        'order': 1,
                    },
                    {
                        'name': 'Prototype & Classes',
                        'explanation': 'JavaScript uses prototype-based inheritance. ES6 classes are syntactic sugar over prototypes, making OOP patterns more familiar.',
                        'example': 'class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    speak() {\n        return `${this.name} makes a noise.`;\n    }\n}\nclass Dog extends Animal {\n    speak() {\n        return `${this.name} barks!`;\n    }\n}\nconst d = new Dog("Rex");\nconsole.log(d.speak());',
                        'learning_objective': 'Use ES6 class syntax to implement object-oriented patterns and understand the prototype chain.',
                        'order': 2,
                    },
                    {
                        'name': 'Modules (ESM)',
                        'explanation': 'ES Modules allow splitting code into reusable files using import and export statements.',
                        'example': '// math.js\nexport const add = (a, b) => a + b;\nexport default function multiply(a, b) { return a * b; }\n\n// main.js\nimport multiply, { add } from "./math.js";\nconsole.log(add(2, 3));     // 5\nconsole.log(multiply(2, 3)); // 6',
                        'learning_objective': 'Organize JavaScript code into modules using ES6 import/export syntax for better code organization.',
                        'order': 3,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Advanced JavaScript',
                'description': 'Event loop, performance patterns, and design patterns.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Event Loop & Concurrency',
                        'explanation': 'JavaScript is single-threaded with an event loop. Understanding the call stack, task queue, and microtask queue is essential for async mastery.',
                        'example': 'console.log("1");\nsetTimeout(() => console.log("2"), 0);\nPromise.resolve().then(() => console.log("3"));\nconsole.log("4");\n// Output: 1, 4, 3, 2\n// Microtasks (Promises) run before macrotasks (setTimeout)',
                        'learning_objective': 'Explain how the JavaScript event loop works and predict execution order of synchronous, Promise, and setTimeout code.',
                        'order': 1,
                    },
                    {
                        'name': 'Design Patterns',
                        'explanation': 'Design patterns are reusable solutions to common problems. Common JS patterns include Observer, Module, Factory, and Singleton.',
                        'example': '// Observer Pattern\nclass EventEmitter {\n    constructor() { this.events = {}; }\n    on(event, cb) {\n        (this.events[event] ||= []).push(cb);\n    }\n    emit(event, data) {\n        (this.events[event] || []).forEach(cb => cb(data));\n    }\n}',
                        'learning_objective': 'Implement common JavaScript design patterns to write maintainable, scalable code.',
                        'order': 2,
                    },
                ]
            },
        ]
    },
    {
        'name': 'React',
        'description': 'A popular JavaScript library for building dynamic, component-based user interfaces.',
        'icon': 'react',
        'color': 'info',
        'order': 3,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'React Basics',
                'description': 'Components, JSX, props, state, and event handling.',
                'order': 1,
                'topics': [
                    {
                        'name': 'Components & JSX',
                        'explanation': 'React apps are built from components — reusable UI pieces. JSX is a syntax extension that looks like HTML inside JavaScript.',
                        'example': 'function Welcome({ name }) {\n    return (\n        <div className="card">\n            <h1>Hello, {name}!</h1>\n            <p>Welcome to React.</p>\n        </div>\n    );\n}\n\nexport default Welcome;',
                        'learning_objective': 'Create functional React components using JSX syntax and understand the component-based architecture.',
                        'order': 1,
                    },
                    {
                        'name': 'State with useState',
                        'explanation': 'useState is a React Hook that lets functional components manage local state. State changes trigger re-renders.',
                        'example': 'import { useState } from "react";\n\nfunction Counter() {\n    const [count, setCount] = useState(0);\n    return (\n        <div>\n            <p>Count: {count}</p>\n            <button onClick={() => setCount(count + 1)}>+</button>\n            <button onClick={() => setCount(count - 1)}>-</button>\n        </div>\n    );\n}',
                        'learning_objective': 'Use the useState hook to add and manage local state in functional components.',
                        'order': 2,
                    },
                    {
                        'name': 'useEffect Hook',
                        'explanation': 'useEffect lets you perform side effects (API calls, subscriptions, timers) in functional components.',
                        'example': 'import { useState, useEffect } from "react";\n\nfunction UserList() {\n    const [users, setUsers] = useState([]);\n    useEffect(() => {\n        fetch("/api/users")\n            .then(r => r.json())\n            .then(setUsers);\n    }, []); // [] means run once on mount\n    return <ul>{users.map(u => <li key={u.id}>{u.name}</li>)}</ul>;\n}',
                        'learning_objective': 'Use useEffect to handle side effects like data fetching, subscriptions, and DOM manipulation.',
                        'order': 3,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'React Patterns',
                'description': 'Context, custom hooks, routing, and state management.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Context API',
                        'explanation': 'React Context provides a way to share data between components without prop drilling.',
                        'example': 'const ThemeContext = React.createContext();\n\nfunction App() {\n    const [theme, setTheme] = useState("light");\n    return (\n        <ThemeContext.Provider value={{ theme, setTheme }}>\n            <Header />\n        </ThemeContext.Provider>\n    );\n}\n\nfunction Header() {\n    const { theme } = useContext(ThemeContext);\n    return <nav className={theme}>...</nav>;\n}',
                        'learning_objective': 'Use the Context API to share state across component trees without prop drilling.',
                        'order': 1,
                    },
                    {
                        'name': 'Custom Hooks',
                        'explanation': 'Custom Hooks are functions starting with "use" that encapsulate and reuse stateful logic across components.',
                        'example': 'function useFetch(url) {\n    const [data, setData] = useState(null);\n    const [loading, setLoading] = useState(true);\n    const [error, setError] = useState(null);\n    useEffect(() => {\n        fetch(url).then(r => r.json())\n            .then(setData).catch(setError)\n            .finally(() => setLoading(false));\n    }, [url]);\n    return { data, loading, error };\n}',
                        'learning_objective': 'Extract and reuse component logic into custom hooks to keep components clean and DRY.',
                        'order': 2,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Advanced React',
                'description': 'Performance optimization, server components, and testing.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Performance Optimization',
                        'explanation': 'React.memo, useMemo, and useCallback prevent unnecessary re-renders and computations.',
                        'example': 'const ExpensiveComponent = React.memo(({ data }) => {\n    return <div>{data.map(item => <Item key={item.id} {...item} />)}</div>;\n});\n\nconst memoizedValue = useMemo(() => {\n    return heavyComputation(data);\n}, [data]);\n\nconst memoizedCallback = useCallback(() => {\n    handleClick(id);\n}, [id]);',
                        'learning_objective': 'Apply React.memo, useMemo, and useCallback to optimize component rendering performance.',
                        'order': 1,
                    },
                ]
            },
        ]
    },
    {
        'name': 'Django',
        'description': 'A high-level Python web framework for rapid, secure web development with a built-in ORM and admin.',
        'icon': 'django',
        'color': 'success',
        'order': 4,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'Django Basics',
                'description': 'Learn Django project structure, models, views, and templates.',
                'order': 1,
                'topics': [
                    {
                        'name': 'Project Setup & Structure',
                        'explanation': 'A Django project contains settings, URLs, and multiple apps. Each app handles a specific feature area.',
                        'example': 'django-admin startproject myproject\ncd myproject\npython manage.py startapp blog\n# Edit settings.py → INSTALLED_APPS → add "blog"\npython manage.py runserver',
                        'learning_objective': 'Create a Django project and app, understand the project structure, and run the development server.',
                        'order': 1,
                    },
                    {
                        'name': 'Models & ORM',
                        'explanation': 'Django models define your database schema as Python classes. The ORM lets you query the database using Python instead of SQL.',
                        'example': 'class Post(models.Model):\n    title = models.CharField(max_length=200)\n    content = models.TextField()\n    created_at = models.DateTimeField(auto_now_add=True)\n\n    def __str__(self):\n        return self.title\n\n# Query: Post.objects.filter(title__contains="Django")',
                        'learning_objective': 'Define database models using Django ORM and perform CRUD operations using the ORM\'s query API.',
                        'order': 2,
                    },
                    {
                        'name': 'Views & URLs',
                        'explanation': 'Views handle HTTP requests and return responses. URLs route requests to the correct view function or class.',
                        'example': '# views.py\ndef post_list(request):\n    posts = Post.objects.all()\n    return render(request, "blog/list.html", {"posts": posts})\n\n# urls.py\nurlpatterns = [\n    path("posts/", views.post_list, name="post-list"),\n    path("posts/<int:pk>/", views.post_detail, name="post-detail"),\n]',
                        'learning_objective': 'Create function-based views, connect them to URL patterns, and render templates with context data.',
                        'order': 3,
                    },
                    {
                        'name': 'Templates & Template Tags',
                        'explanation': 'Django templates use a simple syntax with {{ variables }}, {% tags %}, and filters to render dynamic HTML.',
                        'example': '{# templates/blog/list.html #}\n{% extends "base.html" %}\n{% block content %}\n    {% for post in posts %}\n        <h2>{{ post.title }}</h2>\n        <p>{{ post.content|truncatewords:50 }}</p>\n        <small>{{ post.created_at|date:"M d, Y" }}</small>\n    {% empty %}\n        <p>No posts yet.</p>\n    {% endfor %}\n{% endblock %}',
                        'learning_objective': 'Use Django\'s template language to render dynamic HTML with loops, conditions, filters, and template inheritance.',
                        'order': 4,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'Django Forms & Auth',
                'description': 'Forms, authentication, class-based views, and the Django admin.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Forms & ModelForms',
                        'explanation': 'Django forms handle user input validation. ModelForms automatically create forms from models.',
                        'example': 'class PostForm(ModelForm):\n    class Meta:\n        model = Post\n        fields = ["title", "content"]\n\ndef create_post(request):\n    if request.method == "POST":\n        form = PostForm(request.POST)\n        if form.is_valid():\n            form.save()\n            return redirect("post-list")\n    else:\n        form = PostForm()\n    return render(request, "create.html", {"form": form})',
                        'learning_objective': 'Build and validate HTML forms using Django\'s form system and ModelForms for database-backed forms.',
                        'order': 1,
                    },
                    {
                        'name': 'Authentication & Permissions',
                        'explanation': 'Django provides built-in user authentication with login, logout, registration, and the @login_required decorator.',
                        'example': 'from django.contrib.auth.decorators import login_required\nfrom django.contrib.auth import login, authenticate\n\n@login_required\ndef profile(request):\n    return render(request, "profile.html")\n\ndef login_view(request):\n    user = authenticate(username=username, password=password)\n    if user:\n        login(request, user)\n        return redirect("dashboard")',
                        'learning_objective': 'Implement user authentication with login/logout, protect views with login_required, and manage user permissions.',
                        'order': 2,
                    },
                    {
                        'name': 'Class-Based Views (CBV)',
                        'explanation': 'CBVs provide reusable, extensible view classes for common patterns like list views, detail views, and CRUD operations.',
                        'example': 'from django.views.generic import ListView, DetailView, CreateView\n\nclass PostListView(ListView):\n    model = Post\n    template_name = "blog/list.html"\n    context_object_name = "posts"\n    paginate_by = 10\n\nclass PostCreateView(CreateView):\n    model = Post\n    fields = ["title", "content"]\n    success_url = reverse_lazy("post-list")',
                        'learning_objective': 'Use Django\'s generic class-based views to implement common patterns like CRUD operations with less boilerplate.',
                        'order': 3,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Advanced Django',
                'description': 'REST APIs, Celery, caching, and deployment best practices.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Django REST Framework',
                        'explanation': 'DRF is the standard library for building REST APIs in Django with serializers, viewsets, and authentication.',
                        'example': 'from rest_framework import serializers, viewsets\n\nclass PostSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Post\n        fields = ["id", "title", "content", "created_at"]\n\nclass PostViewSet(viewsets.ModelViewSet):\n    queryset = Post.objects.all()\n    serializer_class = PostSerializer',
                        'learning_objective': 'Build RESTful APIs using Django REST Framework with serializers, viewsets, and proper HTTP methods.',
                        'order': 1,
                    },
                    {
                        'name': 'Celery & Background Tasks',
                        'explanation': 'Celery enables asynchronous task processing in Django, offloading long-running jobs to background workers.',
                        'example': '# tasks.py\nfrom celery import shared_task\n\n@shared_task\ndef send_welcome_email(user_id):\n    user = User.objects.get(id=user_id)\n    # send email here...\n    return f"Email sent to {user.email}"\n\n# views.py - call asynchronously\nsend_welcome_email.delay(user.id)',
                        'learning_objective': 'Configure Celery with Django to run background tasks asynchronously for email sending, report generation, etc.',
                        'order': 2,
                    },
                ]
            },
        ]
    },
    {
        'name': 'Machine Learning',
        'description': 'Learn to build intelligent systems using algorithms, data preprocessing, and predictive modeling.',
        'icon': 'cpu',
        'color': 'danger',
        'order': 5,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'ML Fundamentals',
                'description': 'Data preprocessing, NumPy, Pandas, and basic algorithms.',
                'order': 1,
                'topics': [
                    {
                        'name': 'NumPy & Arrays',
                        'explanation': 'NumPy provides efficient multi-dimensional arrays and mathematical functions essential for ML computations.',
                        'example': 'import numpy as np\n\na = np.array([[1, 2, 3], [4, 5, 6]])\nprint(a.shape)  # (2, 3)\nprint(a.mean())  # 3.5\nprint(a * 2)  # Element-wise multiplication\nprint(np.dot(a, a.T))  # Matrix multiplication',
                        'learning_objective': 'Use NumPy arrays for efficient numerical computing including array operations, slicing, and linear algebra.',
                        'order': 1,
                    },
                    {
                        'name': 'Pandas for Data Analysis',
                        'explanation': 'Pandas provides DataFrames for structured data manipulation, cleaning, and analysis.',
                        'example': 'import pandas as pd\n\ndf = pd.read_csv("data.csv")\nprint(df.head())\nprint(df.describe())\ndf_clean = df.dropna()\ndf["age_group"] = pd.cut(df["age"], bins=[0, 18, 65, 100])\nprint(df.groupby("age_group")["salary"].mean())',
                        'learning_objective': 'Load, clean, transform, and analyze datasets using Pandas DataFrames and Series.',
                        'order': 2,
                    },
                    {
                        'name': 'Linear Regression',
                        'explanation': 'Linear regression predicts a continuous target variable by finding the best-fit line through training data.',
                        'example': 'from sklearn.linear_model import LinearRegression\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.metrics import mean_squared_error\n\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)\nmse = mean_squared_error(y_test, predictions)',
                        'learning_objective': 'Implement linear regression, split data for training/testing, and evaluate model performance.',
                        'order': 3,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'ML Algorithms',
                'description': 'Classification, clustering, ensemble methods, and model evaluation.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Classification Algorithms',
                        'explanation': 'Classification predicts categorical labels. Common algorithms include Decision Trees, Random Forests, and SVM.',
                        'example': 'from sklearn.ensemble import RandomForestClassifier\nfrom sklearn.metrics import classification_report\n\nrf = RandomForestClassifier(n_estimators=100, random_state=42)\nrf.fit(X_train, y_train)\ny_pred = rf.predict(X_test)\nprint(classification_report(y_test, y_pred))\n# Feature importance\nprint(rf.feature_importances_)',
                        'learning_objective': 'Train and evaluate classification models and interpret performance metrics like precision, recall, and F1-score.',
                        'order': 1,
                    },
                    {
                        'name': 'Model Evaluation & Cross-Validation',
                        'explanation': 'Cross-validation gives a more reliable estimate of model performance by training on multiple data splits.',
                        'example': 'from sklearn.model_selection import cross_val_score, GridSearchCV\n\nscores = cross_val_score(model, X, y, cv=5, scoring="accuracy")\nprint(f"Accuracy: {scores.mean():.2f} ± {scores.std():.2f}")\n\nparam_grid = {"n_estimators": [50, 100, 200], "max_depth": [3, 5, None]}\ngrid_search = GridSearchCV(rf, param_grid, cv=5)\ngrid_search.fit(X_train, y_train)',
                        'learning_objective': 'Apply cross-validation and hyperparameter tuning to build robust, well-generalized ML models.',
                        'order': 2,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Deep Learning',
                'description': 'Neural networks, CNNs, RNNs, and Transformer architectures.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Neural Networks with PyTorch',
                        'explanation': 'PyTorch is a flexible deep learning framework. Neural networks are built from layers of connected neurons that learn from data.',
                        'example': 'import torch\nimport torch.nn as nn\n\nclass Network(nn.Module):\n    def __init__(self):\n        super().__init__()\n        self.layers = nn.Sequential(\n            nn.Linear(784, 256),\n            nn.ReLU(),\n            nn.Linear(256, 10)\n        )\n    def forward(self, x):\n        return self.layers(x)',
                        'learning_objective': 'Build, train, and evaluate neural networks using PyTorch for classification and regression tasks.',
                        'order': 1,
                    },
                ]
            },
        ]
    },
    {
        'name': 'SQL & Databases',
        'description': 'Master relational databases, SQL queries, indexing, and database design principles.',
        'icon': 'database',
        'color': 'secondary',
        'order': 6,
        'roadmaps': [
            {
                'level': 'beginner',
                'title': 'SQL Basics',
                'description': 'SELECT, INSERT, UPDATE, DELETE, and basic JOIN operations.',
                'order': 1,
                'topics': [
                    {
                        'name': 'SELECT & Filtering',
                        'explanation': 'SELECT retrieves data from tables. WHERE clause filters rows. ORDER BY sorts results.',
                        'example': 'SELECT name, email, age\nFROM users\nWHERE age > 18\n  AND city = "New York"\nORDER BY age DESC\nLIMIT 10;',
                        'learning_objective': 'Write SELECT queries with WHERE, ORDER BY, and LIMIT clauses to retrieve and filter database records.',
                        'order': 1,
                    },
                    {
                        'name': 'JOINs',
                        'explanation': 'JOINs combine rows from multiple tables based on a related column. INNER, LEFT, RIGHT, and FULL joins have different behaviors.',
                        'example': 'SELECT u.name, o.total, o.created_at\nFROM users u\nINNER JOIN orders o ON u.id = o.user_id\nWHERE o.total > 100\nORDER BY o.created_at DESC;',
                        'learning_objective': 'Use different JOIN types (INNER, LEFT, RIGHT) to combine data from multiple related tables.',
                        'order': 2,
                    },
                    {
                        'name': 'Aggregations & GROUP BY',
                        'explanation': 'Aggregate functions (COUNT, SUM, AVG, MAX, MIN) summarize data. GROUP BY groups rows with the same values.',
                        'example': 'SELECT\n    department,\n    COUNT(*) AS employee_count,\n    AVG(salary) AS avg_salary,\n    MAX(salary) AS max_salary\nFROM employees\nGROUP BY department\nHAVING COUNT(*) > 5\nORDER BY avg_salary DESC;',
                        'learning_objective': 'Use aggregate functions with GROUP BY and HAVING to produce summary statistics from data.',
                        'order': 3,
                    },
                ]
            },
            {
                'level': 'intermediate',
                'title': 'Advanced SQL',
                'description': 'Subqueries, CTEs, window functions, and indexing.',
                'order': 2,
                'topics': [
                    {
                        'name': 'Window Functions',
                        'explanation': 'Window functions perform calculations across a set of rows related to the current row without collapsing them like GROUP BY.',
                        'example': 'SELECT\n    name,\n    department,\n    salary,\n    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,\n    AVG(salary) OVER (PARTITION BY department) AS dept_avg\nFROM employees;',
                        'learning_objective': 'Use window functions (RANK, ROW_NUMBER, LAG, LEAD, etc.) for advanced analytical queries.',
                        'order': 1,
                    },
                    {
                        'name': 'Indexing & Query Optimization',
                        'explanation': 'Indexes speed up data retrieval. EXPLAIN ANALYZE reveals query execution plans to identify bottlenecks.',
                        'example': '-- Create index\nCREATE INDEX idx_users_email ON users(email);\nCREATE INDEX idx_orders_user_date ON orders(user_id, created_at);\n\n-- Analyze query performance\nEXPLAIN ANALYZE\nSELECT * FROM orders WHERE user_id = 123;',
                        'learning_objective': 'Create appropriate indexes and use EXPLAIN to analyze and optimize slow database queries.',
                        'order': 2,
                    },
                ]
            },
            {
                'level': 'advanced',
                'title': 'Database Design & Architecture',
                'description': 'Normalization, transactions, replication, and NoSQL.',
                'order': 3,
                'topics': [
                    {
                        'name': 'Transactions & ACID',
                        'explanation': 'Transactions group multiple operations that must all succeed or all fail. ACID properties ensure data integrity.',
                        'example': 'BEGIN;\n\n-- Transfer $100 from account A to B\nUPDATE accounts SET balance = balance - 100 WHERE id = 1;\nUPDATE accounts SET balance = balance + 100 WHERE id = 2;\n\n-- Only commit if both succeed\nCOMMIT;\n-- Or rollback on error: ROLLBACK;',
                        'learning_objective': 'Use database transactions to maintain data integrity and understand ACID properties (Atomicity, Consistency, Isolation, Durability).',
                        'order': 1,
                    },
                ]
            },
        ]
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with technologies, roadmaps, and topics'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        for tech_data in TECHNOLOGIES:
            roadmaps_data = tech_data.pop('roadmaps')
            tech, created = Technology.objects.update_or_create(
                name=tech_data['name'],
                defaults=tech_data
            )
            if created:
                self.stdout.write(f'  Created technology: {tech.name}')
            else:
                self.stdout.write(f'  Updated technology: {tech.name}')

            for rm_data in roadmaps_data:
                topics_data = rm_data.pop('topics')
                roadmap, _ = Roadmap.objects.update_or_create(
                    technology=tech,
                    level=rm_data['level'],
                    defaults=rm_data
                )
                for topic_data in topics_data:
                    Topic.objects.update_or_create(
                        roadmap=roadmap,
                        name=topic_data['name'],
                        defaults=topic_data
                    )

            tech_data['roadmaps'] = roadmaps_data

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
