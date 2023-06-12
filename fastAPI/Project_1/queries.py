    qr = db.query(Student).all()
    qr = db.query(Student.name, Student.course).filter(Student.name.in_(['hussain','valli']))
    qr = db.query(Student).filter(and_(Student.age >= 27, Student.age <=30)).all()
    qr = db.query(Student).filter(or_(Student.age >= 27, Student.age <=30)).all()
    qr = db.query(Student).filter(Student.age.between(27,30)).all()
    qr = db.query(Student).filter(Student.age.between(27,30)).all()
    qr = db.query(Student)
    qr.filter(Student.age.notin_([26,28])).all()
    qr.filter(Student.name.like('%hu%'))
    qr.filter(Student.name.notlike('%hu%')).all()
    qr.filter(Student.name.is_(None))
    qr.filter(Student.name.isnot(None))
    qr.filter(Student.name.startswith('h')).all()
    qr.filter(Student.name.endswith('l')).all()
    qr.filter(Student.name.contains('il')).all()
    

### Joins
    se.query(Company).join(Employee).all()
    se.query(Company).join(Employee).filter(and_(Company.name=='google',Employee.age>=26)).one().employees
    se.query(Company).outerjoin(Employee).all() # left outer join

### textual SQL
    from sqlalchemy import text

    se.query(Company).filter(text("id>=2")).all()
    se.query(Company).filter(text("id>=2")).order_by(text('id')).all()
    se.query(Company).filter(text("id>=:value and name=:name")).params(value=2, name='infosys').all()

### func

    from sqlalchemy import func

    se.query(Company.name, func.count(Company.name)).group_by(Company.name).all()
    se.query(Company.name, func.count(Employee.name)).join(Employee).group_by(Company.name).all() # count
    se.query(func.max(Employee.salary)).select_from(Employee).all()  # max
    se.query(func.min(Employee.salary)).select_from(Employee).all() # min
    se.query(func.sum(Employee.salary)).select_from(Employee).all() # sum

## union, union_all

    se.query(Company).union(se.query(Employee)).all()
    se.query(Company).union_all(se.query(Employee)).all()