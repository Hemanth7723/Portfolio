import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace Services section
services_pattern = r'(<section class="ftco-section" id="services-section">.*?</section>)'
services_match = re.search(services_pattern, content, re.DOTALL)
if services_match:
    original = services_match.group(1)
    # Wrap content in bento container
    bento_services = """
<section class="ftco-section" id="services-section">
    <div class="container">
        <div class="row justify-content-center py-5 mt-5">
          <div class="col-md-12 heading-section text-center ftco-animate">
            <h1 class="big big-2">Services</h1>
            <h2 class="mb-4">Services</h2>
          </div>
        </div>
        <div class="bento-container">
            <div class="bento-item wide">
                <div class="services-1">
                    <span class="icon"><i class="flaticon-analysis"></i></span>
                    <div class="desc">
                        <h3 class="mb-5">Test Automation</h3>
                    </div>
                </div>
            </div>
            <div class="bento-item">
                <div class="services-1">
                    <span class="icon"><i class="flaticon-flasks"></i></span>
                    <div class="desc">
                        <h3 class="mb-5">Devops Automation</h3>
                    </div>
                </div>
            </div>
            <div class="bento-item">
                <div class="services-1">
                    <span class="icon"><i class="flaticon-ideas"></i></span>
                    <div class="desc">
                        <h3 class="mb-5">Web Development</h3>
                    </div>
                </div>
            </div>
            <div class="bento-item">
                <div class="services-1">
                    <span class="icon"><i class="flaticon-analysis"></i></span>
                    <div class="desc">
                        <h3 class="mb-5">Flutter Development</h3>
                    </div>
                </div>
            </div>
            <div class="bento-item wide">
                <div class="services-1">
                    <span class="icon"><i class="flaticon-flasks"></i></span>
                    <div class="desc">
                        <h3 class="mb-5">SpringBoot Application Services</h3>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    content = content.replace(original, bento_services)

with open('index.html', 'w') as f:
    f.write(content)
