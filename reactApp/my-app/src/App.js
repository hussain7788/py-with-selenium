import logo from './logo.svg';
import './App.css';
import Func from './components/funcomponent';
import MyClass from './components/classcomponent';
import Name from './components/Name';
import Example from './components/Array';
import Class_Array from './components/Class_Array'
import Forms from './components/Forms';
import Inc_dec from './components/inc_dec';

function App() {
  function AppClick() {
    alert("app.js clicked")
  }
  return (
    <div className="container">
        <p>
          hello world..
          {/* <Func name = "hussain"/>
          <Name/> */}
          {/* <Example names={['python', 'djnago', 'java', 'angular', 'react']}/> */}
          {/* <Class_Array names={['react', 'react native','django']}/> */}
          {/* <Name/> */}
          {/* <Func name="valli"/> */}
          <Forms/>
          {/* <MyClass my_email="email.com" myclick={AppClick}/> */}
          <Inc_dec/>
          
        </p>
    </div>
  );
}

export default App;
