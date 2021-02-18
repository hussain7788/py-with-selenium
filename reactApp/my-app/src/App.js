import logo from './logo.svg';
import './App.css';
import Func from './components/funcomponent';
import MyClass from './components/classcomponent';
import Name from './components/Name';
import Example from './components/Array';
import Class_Array from './components/Class_Array'
import Forms from './components/Forms';

function App() {
  function AppClick() {
    alert("app.js clicked")
  }
  return (
    <div className="container">
        <p>
          hello world..
          {/* <Func name = "hussain"/>
          <MyClass my_emai="email.com" myclick={AppClick}/>
          <Name/> */}
          {/* <Example names={['python', 'djnago', 'java', 'angular', 'react']}/> */}
          <Class_Array names={['react', 'react native','django']}/>
          <Forms />
        </p>
    </div>
  );
}

export default App;
