
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AWS CI/CD Project</title>

        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0b1120;
                color: #f1f5f9;
            }

            nav {
                padding: 22px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid #26334a;
            }

            .logo {
                font-size: 23px;
                font-weight: bold;
                color: #60a5fa;
            }

            .badge {
                color: #4ade80;
                background: #14352b;
                border: 1px solid #226447;
                padding: 9px 14px;
                border-radius: 25px;
                font-size: 12px;
            }

            .hero {
                max-width: 1000px;
                margin: auto;
                padding: 85px 25px 55px;
                text-align: center;
            }

            .eyebrow {
                color: #60a5fa;
                font-size: 13px;
                letter-spacing: 3px;
                font-weight: bold;
            }

            h1 {
                font-size: clamp(36px, 6vw, 60px);
                line-height: 1.15;
                margin: 25px 0 18px;
            }

            h1 span {
                color: #60a5fa;
            }

            .description {
                max-width: 650px;
                margin: auto;
                color: #9caec8;
                line-height: 1.8;
                font-size: 16px;
            }

            .button {
                display: inline-block;
                margin-top: 28px;
                padding: 14px 22px;
                border-radius: 9px;
                color: white;
                background: #2563eb;
                text-decoration: none;
                font-weight: bold;
            }

            .section {
                max-width: 1000px;
                margin: auto;
                padding: 10px 25px 60px;
            }

            .section h2 {
                font-size: 23px;
                margin-bottom: 22px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 18px;
            }

            .card {
                padding: 25px;
                border-radius: 15px;
                background: #131e32;
                border: 1px solid #293750;
            }

            .icon {
                font-size: 30px;
            }

            .card h3 {
                margin: 20px 0 10px;
            }

            .card p {
                color: #9caec8;
                font-size: 14px;
                line-height: 1.8;
            }

            .stack {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                margin-top: 22px;
            }

            .stack span {
                padding: 10px 14px;
                border: 1px solid #293750;
                border-radius: 8px;
                background: #131e32;
                color: #cbd5e1;
                font-size: 13px;
            }

            footer {
                text-align: center;
                border-top: 1px solid #26334a;
                padding: 25px;
                color: #8292ab;
                font-size: 13px;
            }

            @media (max-width: 700px) {
                .cards {
                    grid-template-columns: 1fr;
                }

                nav {
                    padding: 18px 20px;
                }

                .hero {
                    padding-top: 60px;
                }
            }
        </style>
    </head>

    <body>
        <nav>
            <div class="logo">☁ CloudOps</div>
            <div class="badge">● APPLICATION ONLINE</div>
        </nav>

        <section class="hero">
            <div class="eyebrow">AWS CLOUD ENGINEERING</div>

            <h1>
                Build. Test. Deploy.<br>
                <span>Automate Everything.</span>
            </h1>

            <p class="description">
                A cloud-hosted application demonstrating Docker
                containerization and CI/CD automation using GitHub Actions
                and Amazon EC2.
            </p>

            <a class="button" href="/health">Check Application Health ↗</a>
        </section>

        <section class="section">
            <h2>Project Architecture</h2>

            <div class="cards">
                <div class="card">
                    <div class="icon">☁️</div>
                    <h3>Amazon EC2</h3>
                    <p>
                        Hosts the application on AWS and makes it
                        accessible through the server's public address.
                    </p>
                </div>

                <div class="card">
                    <div class="icon">📦</div>
                    <h3>Docker</h3>
                    <p>
                        Packages the Flask application and its dependencies
                        into a portable container.
                    </p>
                </div>

                <div class="card">
                    <div class="icon">⚙️</div>
                    <h3>CI/CD Pipeline</h3>
                    <p>
                        Automates configured testing, image building,
                        and deployment through GitHub Actions.
                    </p>
                </div>
            </div>

            <h2 style="margin-top:40px">Technology Stack</h2>

            <div class="stack">
                <span>Python</span>
                <span>Flask</span>
                <span>Docker</span>
                <span>AWS EC2</span>
                <span>Git & GitHub</span>
                <span>GitHub Actions</span>
                <span>CI/CD</span>
                <span>Health Checks</span>
            </div>
        </section>

        <footer>
            CloudOps CI/CD Project · Built with Flask and Docker
        </footer>
    </body>
    </html>
    """)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

