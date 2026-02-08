from flask import Flask, render_template_string

app = Flask(__name__)

portfolio_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Girish | Portfolio</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            background-color: #f4f6f8;
            color: #333;
        }
        header {
            background-color: #1e293b;
            color: white;
            padding: 30px;
            text-align: center;
        }
        section {
            padding: 30px;
            max-width: 900px;
            margin: auto;
            background: white;
            margin-top: 20px;
            border-radius: 10px;
        }
        h2 {
            color: #1e293b;
        }
        ul {
            line-height: 1.8;
        }
        .skills span {
            display: inline-block;
            background: #e2e8f0;
            padding: 8px 12px;
            margin: 6px;
            border-radius: 20px;
        }
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 30px;
            background: #1e293b;
            color: white;
        }
    </style>
</head>
<body>

<header>
    <h1>Girish</h1>
    <p>Engineering Student | Python Developer | Tech Enthusiast</p>
</header>

<section>
    <h2>About Me</h2>
    <p>
        I am Girish, an engineering student who studied at <strong>Government Engineering College, Rajkot (GECR)</strong>.
        I enjoy building software applications and learning new technologies.
        I am passionate about problem-solving, programming, and continuous self-improvement.
    </p>
</section>

<section>
    <h2>Education</h2>
    <ul>
        <li><strong>College:</strong> Government Engineering College, Rajkot (GECR)</li>
        <li><strong>Degree:</strong> Bachelor of Engineering</li>
        <li><strong>Field:</strong> Computer / IT (assumed)</li>
    </ul>
</section>

<section>
    <h2>Skills</h2>
    <div class="skills">
        <span>Python</span>
        <span>Flask</span>
        <span>HTML</span>
        <span>CSS</span>
        <span>JavaScript</span>
        <span>SQL</span>
        <span>Git & GitHub</span>
        <span>Problem Solving</span>
        <span>Basic Data Structures</span>
    </div>
</section>

<section>
    <h2>Projects</h2>
    <ul>
        <li>Personal Portfolio Website using Python Flask</li>
        <li>Student Management System (Python)</li>
        <li>Basic Web Applications using HTML & CSS</li>
    </ul>
</section>

<section>
    <h2>Contact</h2>
    <p>
        📧 Email: girish@example.com <br>
        🌐 GitHub: github.com/girish <br>
        📍 Location: India
    </p>
</section>

<footer>
    <p>© 2026 Girish | Built with Python & Flask</p>
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(portfolio_html)

if __name__ == "__main__":
    app.run(debug=True)
