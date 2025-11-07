## Answer Sheet: Lab09

**Question 1:** What is the purpose of the `@app.route('/health')` decorator in the code?

**Answer:**

The decorator registers the function as the handler for HTTP requests to the /health URL, it maps that URL path to the Python function.

----------------
**Question 2:** In Jinja2, what is the difference between `{{ my_variable }}` and `{% for item in my_list %}`?

**Answer:**

{{ my_variable }} is an expression, it evaluates the expression and inserts its value into the rendered output. While {% for item in my_list %} ... {% endfor %} is a control statement or a tag, it controls template logic (loops, conditionals)

----------------
**Question 3:** In `app.py`, why is it important to use `(?, ?)` and pass the variables as a tuple in the `conn.execute()` command instead of using f-strings to put the variables directly into the SQL string? What is this technique called?

**Answer:**




----------------
**Question 4:** What is the purpose of `event.preventDefault()` in the JavaScript code? What would happen if you removed that line?

**Answer:**




----------------
**Question 5:** In the `Dockerfile`, why is the `CMD` `["flask", "run", "--host=0.0.0.0"]` necessary? Why wouldn't the default `flask run` (which uses host 127.0.0.1) work?

**Answer:**




----------------
**Question 6:** In the `docker-compose.yml` setup, Nginx is configured to `proxy_pass http://flask-app:5000`. How does the Nginx container know the IP address of the `flask-app` container?

**Answer:**



