package multithreading;

import java.util.concurrent.Exchanger;

public class ExchangerDemo {
    public static void main(String[] args) {
      Exchanger<String> ex = new Exchanger<String>();
      new Thread(new ProducerThread(ex)).start();
      new Thread(new ConsumerThread(ex)).start();
    }
  }
  
  class ProducerThread implements Runnable {
    String str;
    Exchanger<String> ex;
    ProducerThread(Exchanger<String> ex){
      this.ex = ex;
      str = new String();
    }
    @Override
    public void run() {
     int i = 0;
      while(true){
        str = "Producer" + ++i;
        try {
          str = ex.exchange(str);
          Thread.sleep(200);
        } catch (InterruptedException e) {
          System.out.println(e);
        }
      }       
    }   
  }
  
  class ConsumerThread implements Runnable {
    String str;
    Exchanger<String> ex;
    ConsumerThread(Exchanger<String> ex){
      this.ex = ex;
    }
    @Override
    public void run() {
      while(true){
        try {
          str = ex.exchange(new String());
          System.out.println("Got from Producer " + str);
          Thread.sleep(100);
        } catch (InterruptedException e) {
          System.out.println(e);
        }
      }        
    }   
  }
