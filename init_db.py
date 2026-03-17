"""
Database Initialization Script
Ye script database tables banata hai aur sample data dalata hai
"""

from flask import Flask
from models import db, User, Skill
from config import Config
import os

def init_database():
    """
    Database aur tables create karta hai
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        print("🚀 Starting database initialization...")
        
        # Create database folder if not exists
        db_folder = os.path.join(os.path.dirname(__file__), 'database')
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)
            print("✅ Database folder created")
        
        # Drop all tables (fresh start)
        db.drop_all()
        print("🗑️  Dropped old tables (if any)")
        
        # Create all tables
        db.create_all()
        print("✅ Created all tables")
        
        # Create admin user
        admin = User(username='admin', email='admin@example.com')
        admin.set_password('admin123')
        db.session.add(admin)
        print("✅ Created admin user")
        print("   Username: admin")
        print("   Password: admin123")
        
        # Create test user
        testuser = User(username='testuser', email='test@example.com')
        testuser.set_password('test123')
        db.session.add(testuser)
        print("✅ Created test user")
        print("   Username: testuser")
        print("   Password: test123")
        
        # Add comprehensive skills
        skills_data = [
            # Programming Languages
            ('Python', 'Programming Languages', 'High-level programming language'),
            ('JavaScript', 'Programming Languages', 'Web programming language'),
            ('Java', 'Programming Languages', 'Object-oriented programming'),
            ('C++', 'Programming Languages', 'System programming language'),
            ('C#', 'Programming Languages', '.NET programming language'),
            ('PHP', 'Programming Languages', 'Server-side scripting'),
            ('Ruby', 'Programming Languages', 'Dynamic programming language'),
            ('Go', 'Programming Languages', 'Google programming language'),
            ('Swift', 'Programming Languages', 'iOS development'),
            ('Kotlin', 'Programming Languages', 'Android development'),
            ('TypeScript', 'Programming Languages', 'JavaScript with types'),
            ('Rust', 'Programming Languages', 'Systems programming'),
            
            # Web Frameworks
            ('React', 'Frameworks', 'JavaScript UI library'),
            ('Angular', 'Frameworks', 'TypeScript web framework'),
            ('Vue.js', 'Frameworks', 'Progressive JavaScript framework'),
            ('Node.js', 'Frameworks', 'JavaScript runtime'),
            ('Django', 'Frameworks', 'Python web framework'),
            ('Flask', 'Frameworks', 'Python micro-framework'),
            ('Spring', 'Frameworks', 'Java framework'),
            ('Express', 'Frameworks', 'Node.js framework'),
            ('Laravel', 'Frameworks', 'PHP framework'),
            ('Ruby on Rails', 'Frameworks', 'Ruby web framework'),
            ('Next.js', 'Frameworks', 'React framework'),
            ('ASP.NET', 'Frameworks', '.NET framework'),
            
            # Databases
            ('SQL', 'Databases', 'Structured query language'),
            ('MongoDB', 'Databases', 'NoSQL database'),
            ('PostgreSQL', 'Databases', 'Relational database'),
            ('MySQL', 'Databases', 'Relational database'),
            ('Redis', 'Databases', 'In-memory data store'),
            ('Oracle', 'Databases', 'Enterprise database'),
            ('SQLite', 'Databases', 'Lightweight database'),
            ('Cassandra', 'Databases', 'Distributed database'),
            ('Firebase', 'Databases', 'Google database platform'),
            
            # Cloud & DevOps
            ('Docker', 'Cloud', 'Containerization platform'),
            ('Kubernetes', 'Cloud', 'Container orchestration'),
            ('AWS', 'Cloud', 'Amazon cloud services'),
            ('Azure', 'Cloud', 'Microsoft cloud platform'),
            ('GCP', 'Cloud', 'Google cloud platform'),
            ('Jenkins', 'Cloud', 'CI/CD automation'),
            ('Terraform', 'Cloud', 'Infrastructure as code'),
            ('Ansible', 'Cloud', 'Configuration management'),
            
            # Tools & Others
            ('Git', 'Tools', 'Version control system'),
            ('Linux', 'Tools', 'Operating system'),
            ('REST API', 'Tools', 'API architecture'),
            ('GraphQL', 'Tools', 'Query language for APIs'),
            ('HTML', 'Tools', 'Markup language'),
            ('CSS', 'Tools', 'Styling language'),
            ('Sass', 'Tools', 'CSS preprocessor'),
            ('Webpack', 'Tools', 'Module bundler'),
            ('jQuery', 'Tools', 'JavaScript library'),
            
            # Data Science & AI
            ('Machine Learning', 'Data Science', 'AI algorithms'),
            ('Data Science', 'Data Science', 'Data analysis'),
            ('TensorFlow', 'Data Science', 'ML framework'),
            ('PyTorch', 'Data Science', 'ML framework'),
            ('Pandas', 'Data Science', 'Data manipulation'),
            ('NumPy', 'Data Science', 'Numerical computing'),
            ('Scikit-learn', 'Data Science', 'ML library'),
            
            # Mobile Development
            ('React Native', 'Mobile', 'Mobile app framework'),
            ('Flutter', 'Mobile', 'Cross-platform framework'),
            ('iOS Development', 'Mobile', 'Apple platform'),
            ('Android Development', 'Mobile', 'Google platform'),
            
            # Other Skills
            ('Agile', 'Methodology', 'Project management'),
            ('Scrum', 'Methodology', 'Agile framework'),
            ('DevOps', 'Methodology', 'Development operations'),
            ('Testing', 'Methodology', 'Software testing'),
            ('CI/CD', 'Methodology', 'Continuous integration'),
        ]
        
        skill_count = 0
        for name, category, description in skills_data:
            skill = Skill(name=name, category=category, description=description)
            db.session.add(skill)
            skill_count += 1
        
        print(f"✅ Added {skill_count} sample skills")
        
        # Commit all changes
        db.session.commit()
        print("✅ Database committed successfully")
        
        print("\n" + "="*60)
        print("🎉 Database initialization complete!")
        print("="*60)
        print("\n📝 You can now login with:")
        print("   Admin: admin / admin123")
        print("   User: testuser / test123")
        print("\n")

if __name__ == "__main__":
    init_database()