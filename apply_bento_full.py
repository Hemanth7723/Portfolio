import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Skills section
skills_pattern = r'(<section class="ftco-section" id="skills-section">.*?</section>)'
skills_match = re.search(skills_pattern, content, re.DOTALL)
if skills_match:
    original = skills_match.group(1)
    bento_skills = """
<section class="ftco-section" id="skills-section">
    <div class="container">
        <div class="row justify-content-center pb-5">
          <div class="col-md-12 heading-section text-center ftco-animate">
            <h1 class="big big-2">Skills</h1>
            <h2 class="mb-4">My Skills</h2>
          </div>
        </div>
        <div class="bento-container bento-skills">
            <div class="bento-item wide">
                <h3 class="bento-title">Java</h3>
                <div class="progress-wrap ftco-animate">
                    <div class="progress"><div class="progress-bar color-1" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width:90%"></div></div>
                </div>
            </div>
            <div class="bento-item">
                <h3 class="bento-title">Spring Boot</h3>
                <div class="progress-wrap ftco-animate">
                    <div class="progress"><div class="progress-bar color-2" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100" style="width:85%"></div></div>
                </div>
            </div>
            <div class="bento-item">
                <h3 class="bento-title">Microservices</h3>
                <div class="progress-wrap ftco-animate">
                    <div class="progress"><div class="progress-bar color-3" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width:80%"></div></div>
                </div>
            </div>
            <div class="bento-item">
                <h3 class="bento-title">SQL</h3>
                <div class="progress-wrap ftco-animate">
                    <div class="progress"><div class="progress-bar color-4" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width:90%"></div></div>
                </div>
            </div>
            <div class="bento-item wide">
                <h3 class="bento-title">Cloud (AWS/GCP)</h3>
                <div class="progress-wrap ftco-animate">
                    <div class="progress"><div class="progress-bar color-5" role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100" style="width:70%"></div></div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    content = content.replace(original, bento_skills)

# Replace Projects section (simplified bento view)
projects_pattern = r'(<section class="ftco-section" id="projects-section">.*?</section>)'
projects_match = re.search(projects_pattern, content, re.DOTALL)
if projects_match:
    original = projects_match.group(1)
    bento_projects = """
<section class="ftco-section" id="projects-section">
    <div class="container">
        <div class="row justify-content-center mb-5 pb-5">
          <div class="col-md-7 heading-section text-center ftco-animate">
            <h1 class="big big-2">Projects</h1>
            <h2 class="mb-4">My Projects</h2>
          </div>
        </div>
        <div class="bento-container bento-projects">
            <div class="bento-item large">
                <div class="blog-entry justify-content-end">
                    <a href="#" class="block-20" style="background-image: url('images/User_management_System.png');"></a>
                    <div class="text mt-3 float-right d-block">
                        <h3 class="heading">User Management System</h3>
                        <p>Comprehensive system for managing user roles and permissions.</p>
                    </div>
                </div>
            </div>
            <div class="bento-item tall">
                <div class="blog-entry">
                    <a href="#" class="block-20" style="background-image: url('images/Hangman_game.png');"></a>
                    <div class="text mt-3 float-right d-block">
                        <h3 class="heading">Hangman Game</h3>
                        <p>Classic word guessing game implemented in Java.</p>
                    </div>
                </div>
            </div>
            <div class="bento-item wide">
                <div class="blog-entry">
                    <a href="#" class="block-20" style="background-image: url('images/Analysis of Auto-MPG dataset.png');"></a>
                    <div class="text mt-3 float-right d-block">
                        <h3 class="heading">Auto-MPG Dataset Analysis</h3>
                        <p>Data science project analyzing vehicle fuel efficiency.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    content = content.replace(original, bento_projects)

with open('index.html', 'w') as f:
    f.write(content)
