#ifndef _CHAMBERS_H
#define _CHAMBERS_H

using namespace std;

class Chambers
{
    public: 
    String desc;
    int Days[7];
    Time MorningTime;
    Time AfternoonTime;
    Time EveningTime;
    int dosage;
    int current_quantity = 0;
    int dval = 0;

    bool Refill()
    {
      if(current_quantity < 15)
      {
        return true;
      }
      else
      {
        return false;
      }
    }
};

#endif
