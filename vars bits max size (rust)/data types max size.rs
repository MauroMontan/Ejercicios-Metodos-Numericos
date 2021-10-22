use std::convert::TryInto;

fn main() {
    let base:u32 =2; // base
    let arch:u32 =64; //bits
    let mut result:u32; //result

    for i in 0..arch {
        result = base.pow(i.try_into().unwrap());
        
        println!("{}^{} = {}", base,i, result);
  
    }
}